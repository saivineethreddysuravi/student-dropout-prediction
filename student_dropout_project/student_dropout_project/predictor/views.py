import os
import pickle
import pandas as pd

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomUserRegistrationForm, PredictionForm
from .models import UserProfile, PredictionHistory

MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    'predictor',
    'ml_models',
    'best_student_dropout_model.pkl'
)

try:
    with open(MODEL_PATH, 'rb') as f:
        dropout_model = pickle.load(f)
except Exception:
    dropout_model = None

FEATURE_COLUMNS = [
    "marital_status",
    "application_mode",
    "application_order",
    "course",
    "daytime_evening_attendance",
    "previous_qualification",
    "previous_qualification_grade",
    "nacionality",
    "mother_s_qualification",
    "father_s_qualification",
    "mother_s_occupation",
    "father_s_occupation",
    "admission_grade",
    "displaced",
    "educational_special_needs",
    "debtor",
    "tuition_fees_up_to_date",
    "gender",
    "scholarship_holder",
    "age_at_enrollment",
    "international",
    "curricular_units_1st_sem_credited",
    "curricular_units_1st_sem_enrolled",
    "curricular_units_1st_sem_evaluations",
    "curricular_units_1st_sem_approved",
    "curricular_units_1st_sem_grade",
    "curricular_units_1st_sem_without_evaluations",
    "curricular_units_2nd_sem_credited",
    "curricular_units_2nd_sem_enrolled",
    "curricular_units_2nd_sem_evaluations",
    "curricular_units_2nd_sem_approved",
    "curricular_units_2nd_sem_grade",
    "curricular_units_2nd_sem_without_evaluations",
    "unemployment_rate",
    "inflation_rate",
    "gdp",
]

TARGET_MAP = {
    0: 'Dropout',
    1: 'Enrolled',
    2: 'Graduate'
}


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            phone = form.cleaned_data['phone_number']
            dob = form.cleaned_data['date_of_birth']
            UserProfile.objects.create(
                user=user,
                phone_number=phone,
                date_of_birth=dob
            )

            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('predict')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'predictor/register.html', {'form': form})


@login_required
def predict_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            history_obj = form.save(commit=False)
            history_obj.user = request.user

            data_dict = {}
            for col in FEATURE_COLUMNS:
                data_dict[col] = getattr(history_obj, col)

            input_df = pd.DataFrame([data_dict])

            if dropout_model is None:
                messages.error(request, "Model file not found or could not be loaded. Please add the trained model pickle first.")
                return render(request, 'predictor/predict_form.html', {'form': form})

            raw_pred = dropout_model.predict(input_df)[0]
            pred_label = TARGET_MAP.get(raw_pred, str(raw_pred))

            history_obj.prediction_result = pred_label
            history_obj.save()

            messages.success(request, f"Prediction: {pred_label}")
            return redirect('prediction_result', pk=history_obj.pk)
    else:
        form = PredictionForm()

    return render(request, 'predictor/predict_form.html', {'form': form})


@login_required
def prediction_result_view(request, pk):
    prediction = get_object_or_404(PredictionHistory, pk=pk, user=request.user)
    return render(request, 'predictor/prediction_result.html', {'prediction': prediction})


# @login_required
# def history_view(request):
#     history = PredictionHistory.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'predictor/history.html', {'history': history})

# predictor/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import PredictionHistory


@login_required
def history_view(request):
    histories = (
        PredictionHistory.objects
        .filter(user=request.user)
        .order_by('-created_at')        # newest first
    )
    return render(request, 'predictor/history.html', {
        'histories': histories         # 👈 matches the template
    })


@login_required   # remove this if you want it public
def field_info_view(request):
    return render(request, 'predictor/field_info.html')