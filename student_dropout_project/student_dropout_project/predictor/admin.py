from django.contrib import admin
from .models import UserProfile, PredictionHistory

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'date_of_birth')


# @admin.register(PredictionHistory)
# class PredictionHistoryAdmin(admin.ModelAdmin):
#     list_display = ('user', 'prediction_result', 'created_at')
#     list_filter = ('prediction_result', 'created_at')
#     search_fields = ('user__username',)

# predictor/admin.py

from django.contrib import admin
from .models import PredictionHistory


@admin.register(PredictionHistory)
class PredictionHistoryAdmin(admin.ModelAdmin):
    # columns shown in the list page
    list_display = (
        "id",
        "user",
        "created_at",
        "course",
        "application_order",
        "admission_grade",
        "curricular_units_1st_sem_grade",
        "curricular_units_2nd_sem_grade",
        "prediction_result",
    )

    # right-side filters
    list_filter = (
        "prediction_result",
        "course",
        "gender",
        "scholarship_holder",
        "displaced",
        "international",
        "created_at",
    )

    # search box (top right)
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
    )

    # default ordering (newest first)
    ordering = ("-created_at",)

    # fields that cannot be edited in admin
    readonly_fields = ("created_at", "prediction_result")

    # nice grouping inside the edit page
    fieldsets = (
        ("User & Prediction", {
            "fields": ("user", "created_at", "prediction_result")
        }),
        ("Student & Admission Details", {
            "fields": (
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
            )
        }),
        ("Academic Performance – 1st Semester", {
            "fields": (
                "curricular_units_1st_sem_credited",
                "curricular_units_1st_sem_enrolled",
                "curricular_units_1st_sem_evaluations",
                "curricular_units_1st_sem_approved",
                "curricular_units_1st_sem_grade",
                "curricular_units_1st_sem_without_evaluations",
            )
        }),
        ("Academic Performance – 2nd Semester", {
            "fields": (
                "curricular_units_2nd_sem_credited",
                "curricular_units_2nd_sem_enrolled",
                "curricular_units_2nd_sem_evaluations",
                "curricular_units_2nd_sem_approved",
                "curricular_units_2nd_sem_grade",
                "curricular_units_2nd_sem_without_evaluations",
            )
        }),
        ("Economic Context", {
            "fields": (
                "unemployment_rate",
                "inflation_rate",
                "gdp",
            )
        }),
    )


# Optional: customize admin site titles
admin.site.site_header = "Student Dropout Prediction Admin"
admin.site.site_title = "Dropout Prediction Admin"
admin.site.index_title = "Administration"
