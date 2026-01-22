# predictor/forms.py

import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from .models import PredictionHistory


# =========================
#  Registration Form
# =========================

class CustomUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'date_of_birth',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Bootstrap styling
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')

        # Disable future dates in date picker
        today = datetime.date.today().isoformat()
        self.fields['date_of_birth'].widget.attrs['max'] = today

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob and dob > timezone.now().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob


# =========================
#  Prediction Form
# =========================

class PredictionForm(forms.ModelForm):
    # Simple yes/no style (0/1) fields
    YES_NO = (
        (1, "Yes"),
        (0, "No"),
    )

    GENDER_CHOICES = (
        (1, "Male"),
        (0, "Female"),
    )

    DAYTIME_EVENING_CHOICES = (
        (1, "Daytime"),
        (0, "Evening"),
    )

    # Marital status
    MARITAL_STATUS_CHOICES = (
        (1, "Single"),
        (2, "Married"),
        (3, "Widower"),
        (4, "Divorced"),
        (5, "Facto union"),
        (6, "Legally separated"),
    )

    # Application mode
    APPLICATION_MODE_CHOICES = (
        (1, "1st phase - general contingent"),
        (2, "Ordinance No. 612/93"),
        (5, "1st phase - special contingent (Azores Island)"),
        (7, "Holders of other higher courses"),
        (10, "Ordinance No. 854-B/99"),
        (15, "International student (bachelor)"),
        (16, "1st phase - special contingent (Madeira Island)"),
        (17, "2nd phase - general contingent"),
        (18, "3rd phase - general contingent"),
        (26, "Ordinance No. 533-A/99, item b2) (Different Plan)"),
        (27, "Ordinance No. 533-A/99, item b3 (Other Institution)"),
        (39, "Over 23 years old"),
        (42, "Transfer"),
        (43, "Change of course"),
        (44, "Technological specialization diploma holders"),
        (51, "Change of institution/course"),
        (53, "Short cycle diploma holders"),
        (57, "Change of institution/course (International)"),
    )

    # Application order 0–9 (0 = first choice, 9 = last)
    APPLICATION_ORDER_CHOICES = tuple(
        (i, f"{i} (choice {i+1})") for i in range(0, 10)
    )

    # Course
    COURSE_CHOICES = (
        (33, "Biofuel Production Technologies"),
        (171, "Animation and Multimedia Design"),
        (8014, "Social Service (evening attendance)"),
        (9003, "Agronomy"),
        (9070, "Communication Design"),
        (9085, "Veterinary Nursing"),
        (9119, "Informatics Engineering"),
        (9130, "Equinculture"),
        (9147, "Management"),
        (9238, "Social Service"),
        (9254, "Tourism"),
        (9500, "Nursing"),
        (9556, "Oral Hygiene"),
        (9670, "Advertising and Marketing Management"),
        (9773, "Journalism and Communication"),
        (9853, "Basic Education"),
        (9991, "Management (evening attendance)"),
    )

    # Previous qualification
    PREVIOUS_QUALIFICATION_CHOICES = (
        (1, "Secondary education"),
        (2, "Higher education - bachelor's degree"),
        (3, "Higher education - degree"),
        (4, "Higher education - master's"),
        (5, "Higher education - doctorate"),
        (6, "Frequency of higher education"),
        (9, "12th year - not completed"),
        (10, "11th year - not completed"),
        (12, "Other - 11th year"),
        (14, "10th year"),
        (15, "10th year - not completed"),
        (19, "Basic education 3rd cycle (9th/10th/11th) or equiv."),
        (38, "Basic education 2nd cycle (6th/7th/8th) or equiv."),
        (39, "Technological specialization course"),
        (40, "Higher education - degree (1st cycle)"),
        (42, "Professional higher technical course"),
        (43, "Higher education - master (2nd cycle)"),
    )

    # Nationality
    NACIONALITY_CHOICES = (
        (1, "Portuguese"),
        (2, "German"),
        (6, "Spanish"),
        (11, "Italian"),
        (13, "Dutch"),
        (14, "English"),
        (17, "Lithuanian"),
        (21, "Angolan"),
        (22, "Cape Verdean"),
        (24, "Guinean"),
        (25, "Mozambican"),
        (26, "Santomean"),
        (32, "Turkish"),
        (41, "Brazilian"),
        (62, "Romanian"),
        (100, "Moldovan (Republic of)"),
        (101, "Mexican"),
        (103, "Ukrainian"),
        (105, "Russian"),
        (108, "Cuban"),
        (109, "Colombian"),
    )

    # Mother's qualification
    MOTHER_QUAL_CHOICES = (
        (1, "Secondary Education - 12th Year or Eq."),
        (2, "Higher Education - Bachelor's Degree"),
        (3, "Higher Education - Degree"),
        (4, "Higher Education - Master's"),
        (5, "Higher Education - Doctorate"),
        (6, "Frequency of Higher Education"),
        (9, "12th Year - Not Completed"),
        (10, "11th Year - Not Completed"),
        (11, "7th Year (Old)"),
        (12, "Other - 11th Year"),
        (14, "10th Year"),
        (18, "General commerce course"),
        (19, "Basic Education 3rd Cycle"),
        (22, "Technical-professional course"),
        (26, "7th year of schooling"),
        (27, "2nd cycle of general high school course"),
        (29, "9th Year - Not Completed"),
        (30, "8th year of schooling"),
        (34, "Unknown"),
        (35, "Can't read or write"),
        (36, "Can read, no 4th year"),
        (37, "Basic education 1st cycle"),
        (38, "Basic education 2nd cycle"),
        (39, "Technological specialization course"),
        (40, "Higher education - degree (1st cycle)"),
        (41, "Specialized higher studies course"),
        (42, "Professional higher technical course"),
        (43, "Higher Education - Master (2nd cycle)"),
        (44, "Higher Education - Doctorate (3rd cycle)"),
    )

    # Father's qualification
    FATHER_QUAL_CHOICES = (
        (1, "Secondary Education - 12th Year or Eq."),
        (2, "Higher Education - Bachelor's Degree"),
        (3, "Higher Education - Degree"),
        (4, "Higher Education - Master's"),
        (5, "Higher Education - Doctorate"),
        (6, "Frequency of Higher Education"),
        (9, "12th Year - Not Completed"),
        (10, "11th Year - Not Completed"),
        (11, "7th Year (Old)"),
        (12, "Other - 11th Year"),
        (13, "2nd year complementary high school course"),
        (14, "10th Year"),
        (18, "General commerce course"),
        (19, "Basic Education 3rd Cycle"),
        (20, "Complementary High School Course"),
        (22, "Technical-professional course"),
        (25, "Complementary High School - not concluded"),
        (26, "7th year of schooling"),
        (27, "2nd cycle general high school course"),
        (29, "9th Year - Not Completed"),
        (30, "8th year of schooling"),
        (31, "General Course of Administration and Commerce"),
        (33, "Supplementary Accounting and Administration"),
        (34, "Unknown"),
        (35, "Can't read or write"),
        (36, "Can read, no 4th year"),
        (37, "Basic education 1st cycle"),
        (38, "Basic education 2nd cycle"),
        (39, "Technological specialization course"),
        (40, "Higher education - degree (1st cycle)"),
        (41, "Specialized higher studies course"),
        (42, "Professional higher technical course"),
        (43, "Higher Education - Master (2nd cycle)"),
        (44, "Higher Education - Doctorate (3rd cycle)"),
    )

    # Mother's occupation
    MOTHER_OCC_CHOICES = (
        (0, "Student"),
        (1, "Legislative/Executive reps, directors"),
        (2, "Specialists in intellectual & scientific activities"),
        (3, "Intermediate level technicians & professions"),
        (4, "Administrative staff"),
        (5, "Personal services, security & sellers"),
        (6, "Farmers & skilled agriculture/fisheries/forestry"),
        (7, "Skilled industry/construction/crafts workers"),
        (8, "Machine operators & assembly workers"),
        (9, "Unskilled workers"),
        (10, "Armed Forces professions"),
        (90, "Other situation"),
        (99, "(blank)"),
        (122, "Health professionals"),
        (123, "Teachers"),
        (125, "ICT specialists"),
        (131, "Intermediate science/engineering technicians"),
        (132, "Intermediate health technicians"),
        (134, "Intermediate legal/social/sports/cultural"),
        (141, "Office workers, secretaries, data operators"),
        (143, "Data/accounting/financial/registry operators"),
        (144, "Other administrative support staff"),
        (151, "Personal service workers"),
        (152, "Sellers"),
        (153, "Personal care workers"),
        (171, "Skilled construction workers (except electricians)"),
        (173, "Skilled workers in printing/jewelers/artisans"),
        (175, "Workers in food/wood/clothing/other industries"),
        (191, "Cleaning workers"),
        (192, "Unskilled agriculture/animal/fisheries/forestry"),
        (193, "Unskilled extractive/construction/manufacturing/transport"),
        (194, "Meal preparation assistants"),
    )

    # Father's occupation
    FATHER_OCC_CHOICES = (
        (0, "Student"),
        (1, "Legislative/Executive reps, directors"),
        (2, "Specialists in intellectual & scientific activities"),
        (3, "Intermediate level technicians & professions"),
        (4, "Administrative staff"),
        (5, "Personal services, security & sellers"),
        (6, "Farmers & skilled agriculture/fisheries/forestry"),
        (7, "Skilled industry/construction/crafts workers"),
        (8, "Machine operators & assembly workers"),
        (9, "Unskilled workers"),
        (10, "Armed Forces professions"),
        (90, "Other situation"),
        (99, "(blank)"),
        (101, "Armed Forces Officers"),
        (102, "Armed Forces Sergeants"),
        (103, "Other Armed Forces personnel"),
        (112, "Directors of administrative & commercial services"),
        (114, "Hotel/catering/trade/services directors"),
        (121, "Physical sciences/engineering specialists"),
        (122, "Health professionals"),
        (123, "Teachers"),
        (124, "Finance/accounting/admin/PR specialists"),
        (131, "Intermediate science/engineering technicians"),
        (132, "Intermediate health technicians"),
        (134, "Intermediate legal/social/sports/cultural"),
        (135, "ICT technicians"),
        (141, "Office workers, secretaries, data operators"),
        (143, "Data/accounting/financial/registry operators"),
        (144, "Other administrative support staff"),
        (151, "Personal service workers"),
        (152, "Sellers"),
        (153, "Personal care workers"),
        (154, "Protection & security services"),
        (161, "Market-oriented skilled agricultural workers"),
        (163, "Subsistence farmers/livestock/fishers/hunters"),
        (171, "Skilled construction workers (except electricians)"),
        (172, "Skilled metallurgy/metalworking workers"),
        (174, "Skilled electricity/electronics workers"),
        (175, "Workers in food/wood/clothing/other crafts"),
        (181, "Fixed plant & machine operators"),
        (182, "Assembly workers"),
        (183, "Vehicle drivers & mobile equipment operators"),
        (192, "Unskilled agriculture/animal/fisheries/forestry"),
        (193, "Unskilled extractive/construction/manufacturing/transport"),
        (194, "Meal preparation assistants"),
        (195, "Street vendors/service providers"),
    )

    # ==== CATEGORICAL OVERRIDES (dropdowns) ====

    marital_status = forms.TypedChoiceField(
        choices=MARITAL_STATUS_CHOICES, coerce=int,
    )
    application_mode = forms.TypedChoiceField(
        choices=APPLICATION_MODE_CHOICES, coerce=int,
    )
    application_order = forms.TypedChoiceField(
        choices=APPLICATION_ORDER_CHOICES, coerce=int,
    )
    course = forms.TypedChoiceField(
        choices=COURSE_CHOICES, coerce=int,
    )
    daytime_evening_attendance = forms.TypedChoiceField(
        choices=DAYTIME_EVENING_CHOICES, coerce=int,
    )
    previous_qualification = forms.TypedChoiceField(
        choices=PREVIOUS_QUALIFICATION_CHOICES, coerce=int,
    )
    nacionality = forms.TypedChoiceField(
        choices=NACIONALITY_CHOICES, coerce=int,
    )
    mother_s_qualification = forms.TypedChoiceField(
        choices=MOTHER_QUAL_CHOICES, coerce=int,
    )
    father_s_qualification = forms.TypedChoiceField(
        choices=FATHER_QUAL_CHOICES, coerce=int,
    )
    mother_s_occupation = forms.TypedChoiceField(
        choices=MOTHER_OCC_CHOICES, coerce=int,
    )
    father_s_occupation = forms.TypedChoiceField(
        choices=FATHER_OCC_CHOICES, coerce=int,
    )

    displaced = forms.TypedChoiceField(
        choices=YES_NO, coerce=int,
    )
    educational_special_needs = forms.TypedChoiceField(
        choices=YES_NO, coerce=int,
    )
    debtor = forms.TypedChoiceField(
        choices=YES_NO, coerce=int,
    )
    tuition_fees_up_to_date = forms.TypedChoiceField(
        choices=YES_NO, coerce=int,
    )
    gender = forms.TypedChoiceField(
        choices=GENDER_CHOICES, coerce=int,
    )
    scholarship_holder = forms.TypedChoiceField(
        choices=YES_NO, coerce=int,
    )
    international = forms.TypedChoiceField(
        choices=YES_NO, coerce=int,
    )

    # ==== NUMERIC FIELDS WITH RANGES + PLACEHOLDERS ====

    # 1st semester
    curricular_units_1st_sem_credited = forms.IntegerField(
        min_value=0, max_value=20,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 20',
        }),
    )
    curricular_units_1st_sem_enrolled = forms.IntegerField(
        min_value=0, max_value=26,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 26',
        }),
    )
    curricular_units_1st_sem_evaluations = forms.IntegerField(
        min_value=0, max_value=45,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 45',
        }),
    )
    curricular_units_1st_sem_approved = forms.IntegerField(
        min_value=0, max_value=26,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 26',
        }),
    )
    curricular_units_1st_sem_grade = forms.IntegerField(
        min_value=0, max_value=20,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 20',
        }),
    )
    curricular_units_1st_sem_without_evaluations = forms.IntegerField(
        min_value=0, max_value=12,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 12',
        }),
    )

    # 2nd semester
    curricular_units_2nd_sem_credited = forms.IntegerField(
        min_value=0, max_value=19,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 19',
        }),
    )
    curricular_units_2nd_sem_enrolled = forms.IntegerField(
        min_value=0, max_value=23,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 23',
        }),
    )
    curricular_units_2nd_sem_evaluations = forms.IntegerField(
        min_value=0, max_value=33,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 33',
        }),
    )
    curricular_units_2nd_sem_approved = forms.IntegerField(
        min_value=0, max_value=20,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 20',
        }),
    )
    curricular_units_2nd_sem_grade = forms.IntegerField(
        min_value=0, max_value=20,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 20',
        }),
    )
    curricular_units_2nd_sem_without_evaluations = forms.IntegerField(
        min_value=0, max_value=12,
        widget=forms.NumberInput(attrs={
            'placeholder': '0 – 12',
        }),
    )

    # Economic indicators
    unemployment_rate = forms.FloatField(
        min_value=7.6, max_value=16.2,
        widget=forms.NumberInput(attrs={
            'step': '0.1',
            'placeholder': '7.6 – 16.2 (%)',
        }),
    )
    inflation_rate = forms.FloatField(
        min_value=-0.8, max_value=3.7,
        widget=forms.NumberInput(attrs={
            'step': '0.1',
            'placeholder': '-0.8 – 3.7 (%)',
        }),
    )
    gdp = forms.FloatField(
        min_value=-4.06, max_value=3.51,
        widget=forms.NumberInput(attrs={
            'step': '0.01',
            'placeholder': '-4.06 – 3.51',
        }),
    )

    class Meta:
        model = PredictionHistory
        exclude = ['user', 'created_at', 'prediction_result']
        widgets = {
            'previous_qualification_grade': forms.NumberInput(attrs={
                'step': '0.01',
                'placeholder': '0 – 200',
            }),
            'admission_grade': forms.NumberInput(attrs={
                'step': '0.01',
                'placeholder': '0 – 200',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Bootstrap class to all widgets
        for field in self.fields.values():
            css = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (css + ' form-control').strip()
