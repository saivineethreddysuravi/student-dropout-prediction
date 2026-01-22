from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username


class PredictionHistory(models.Model):
    TARGET_CHOICES = [
        ('Dropout', 'Dropout'),
        ('Enrolled', 'Enrolled'),
        ('Graduate', 'Graduate'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    marital_status = models.IntegerField()
    application_mode = models.IntegerField()
    application_order = models.IntegerField()
    course = models.IntegerField()
    daytime_evening_attendance = models.IntegerField()
    previous_qualification = models.IntegerField()
    previous_qualification_grade = models.FloatField()
    nacionality = models.IntegerField()
    mother_s_qualification = models.IntegerField()
    father_s_qualification = models.IntegerField()
    mother_s_occupation = models.IntegerField()
    father_s_occupation = models.IntegerField()
    admission_grade = models.FloatField()
    displaced = models.IntegerField()
    educational_special_needs = models.IntegerField()
    debtor = models.IntegerField()
    tuition_fees_up_to_date = models.IntegerField()
    gender = models.IntegerField()
    scholarship_holder = models.IntegerField()
    age_at_enrollment = models.IntegerField()
    international = models.IntegerField()
    curricular_units_1st_sem_credited = models.IntegerField()
    curricular_units_1st_sem_enrolled = models.IntegerField()
    curricular_units_1st_sem_evaluations = models.IntegerField()
    curricular_units_1st_sem_approved = models.IntegerField()
    curricular_units_1st_sem_grade = models.IntegerField()
    curricular_units_1st_sem_without_evaluations = models.IntegerField()
    curricular_units_2nd_sem_credited = models.IntegerField()
    curricular_units_2nd_sem_enrolled = models.IntegerField()
    curricular_units_2nd_sem_evaluations = models.IntegerField()
    curricular_units_2nd_sem_approved = models.IntegerField()
    curricular_units_2nd_sem_grade = models.IntegerField()
    curricular_units_2nd_sem_without_evaluations = models.IntegerField()
    unemployment_rate = models.FloatField()
    inflation_rate = models.FloatField()
    gdp = models.FloatField()

    prediction_result = models.CharField(max_length=20, choices=TARGET_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.prediction_result} - {self.created_at.strftime('%Y-%m-%d')}"
