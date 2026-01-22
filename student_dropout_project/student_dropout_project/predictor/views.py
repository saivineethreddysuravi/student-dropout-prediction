import os
import pandas as pd
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomUserRegistrationForm, PredictionForm
from .models import UserProfile, PredictionHistory
from .services import PredictionService  # Enterprise Service Pattern

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            UserProfile.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number'],
                date_of_birth=form.cleaned_data['date_of_birth']
            )

            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('predict')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'predictor/register.html', {'form': form})


@login_required
def predict_view(request):
    """
    Handles the prediction request using the PredictionService.
    Follows the 'Thin View, Fat Service' architectural pattern.
    """
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # 1. Create a transient history object (don't save yet)
            history_obj = form.save(commit=False)
            history_obj.user = request.user

            # 2. Extract data for the service
            # (We use the form's cleaned data or the object's attributes)
            # The service expects a dict matching the feature columns
            data_dict = {
                field.name: getattr(history_obj, field.name) 
                for field in PredictionHistory._meta.fields 
                if field.name in PredictionService._feature_columns
            }

            try:
                # 3. Call the Service Layer
                pred_label, metadata = PredictionService.predict(data_dict)

                # 4. Save results
                history_obj.prediction_result = pred_label
                # (Optional) We could save risk_level to the DB if we added a column for it
                history_obj.save()

                # 5. User Feedback
                risk_msg = f"Risk Level: {metadata.get('risk_level', 'N/A')}"
                if metadata.get('risk_drivers'):
                    risk_msg += f" | Factors: {', '.join(metadata['risk_drivers'])}"
                
                messages.success(request, f"Result: {pred_label} ({risk_msg})")
                return redirect('prediction_result', pk=history_obj.pk)

            except FileNotFoundError:
                messages.error(request, "System Error: ML Model file is missing. Please contact admin.")
            except Exception as e:
                messages.error(request, f"Prediction Failed: {str(e)}")
                
    else:
        form = PredictionForm()

    return render(request, 'predictor/predict_form.html', {'form': form})


@login_required
def prediction_result_view(request, pk):
    prediction = get_object_or_404(PredictionHistory, pk=pk, user=request.user)
    return render(request, 'predictor/prediction_result.html', {'prediction': prediction})


@login_required
def history_view(request):
    histories = PredictionHistory.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'predictor/history.html', {'histories': histories})


@login_required
def field_info_view(request):
    return render(request, 'predictor/field_info.html')
