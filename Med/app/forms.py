from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select, SelectMultiple, Textarea, CheckboxInput, NumberInput
from account.models import Account
from app.models import *

class AccountForm(ModelForm):
    class Meta: 
        model = Account
        fields = ['username', 'password', 'surname_doctor', 'name_doctor', 'middlename_doctor', 'positions_doctor']

        widgets = {
            "positions_doctor": Select(attrs={
                'class': 'input_text'
            })
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = ['name_disease', 'description_disease', 'symptoms', 'status_genetic_predisposition', 'description_genetic_predisposition']

        widgets = {
            "symptoms": SelectMultiple(attrs={
                'class': 'input_text symptoms'
            }),

            "name_disease": TextInput(attrs={
            'class': 'input_text'
            }),

            "description_disease": Textarea(attrs={
            'class': 'input_text disease',
            }),

            "description_genetic_predisposition": Textarea(attrs={
            'class': 'input_text disease'
            })
        }

# class DistributionForm(ModelForm):
#     class Meta:
#         model = Distribution
#         fields = '__all__'

#         widgets = {
#             "name_distribution": TextInput(attrs={
#             'class': 'input_text'
#             }),

#             "fk_patient": Select(attrs={
#             'class': 'input_text'
#             }),

#             "fk_doctor": Select(attrs={
#             'class': 'input_text'
#             })
#         }

class SymptomForm(ModelForm):
    class Meta:
        model = Symptom
        fields = '__all__'

        widgets = {
            "name_symptom": TextInput(attrs={
            'class': 'input_text'
            }),

            "description_symptom": Textarea(attrs={
            'class': 'input_text symptom'
            })
        }

class MedicalRecordForm(ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

        widgets = {
            "fk_patient": Select(attrs={
            'class': 'input_text'
            }),

            "diseases": SelectMultiple(attrs={
            'class': 'input_text symptom'
            })
        }


class RecommendationForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        widgets = {
            "description_recommendation": Textarea(attrs={
            'class': 'input_text recommendation'
            }),

            "fk_account": Select(attrs={
            'class': 'input_text',
            }),

            "surname_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "name_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "middlename_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "birthday_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "number_of_medical_card": NumberInput(attrs={
                'class': 'input_text',
            }),

            "gender_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "enlightenment_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "symptoms_patient": SelectMultiple(attrs={
                'class': 'input_text patient'
            }),

            "childhood_diseases": SelectMultiple(attrs={
                'class': 'input_text patient'
            }),

            "relatives_diseases": SelectMultiple(attrs={
                'class': 'input_text patient'
            }),

            "chronic_disease": Textarea(attrs={
            'class': 'input_text patient'
            })
        }


# ПАЦИЕНТ -------------------------------------------------------


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['surname_patient', 'name_patient', 'middlename_patient', 'number_of_medical_card', 'symptoms_patient', 'childhood_diseases', 'relatives_diseases', 'chronic_disease','gender_patient','enlightenment_patient','birthday_patient']

        widgets = {
            "surname_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "name_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "middlename_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "birthday_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "number_of_medical_card": NumberInput(attrs={
                'class': 'input_text',
            }),

            "gender_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "enlightenment_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "symptoms_patient": SelectMultiple(attrs={
                'class': 'input_text patient'
            }),

            "childhood_diseases": SelectMultiple(attrs={
                'class': 'input_text patient'
            }),

            "relatives_diseases": SelectMultiple(attrs={
                'class': 'input_text patient'
            }),

            "chronic_disease": Textarea(attrs={
            'class': 'input_text patient'
            })
        }

