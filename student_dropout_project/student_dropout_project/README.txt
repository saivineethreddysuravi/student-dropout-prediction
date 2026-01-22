Student Dropout Prediction Django Project
=======================================

Setup steps:
1. Install dependencies (no virtualenv needed if you don't want):
   pip install django pandas scikit-learn

2. Place your trained model pickle file at:
   predictor/ml_models/best_student_dropout_model.pkl

   The view will try to load this file and run .predict().
   Make sure the model was trained with the same FEATURE_COLUMNS order as in predictor/views.py.

3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Create a superuser (for admin access):
   python manage.py createsuperuser

5. Run the server:
   python manage.py runserver

URLs:
   /register/  - Custom user registration
   /login/     - Login
   /predict/   - Prediction form (authenticated users)
   /history/   - Logged-in user's prediction history
   /admin/     - Django admin
