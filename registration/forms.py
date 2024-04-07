from django import forms
from django.core.exceptions import ValidationError
from registration.models import Doctor, MedicalHistory, Recommendation, ReasonForVisit, Patient, Visit

class ReasonForm(forms.ModelForm):
    class Meta:
        model = ReasonForVisit
        fields = '__all__'

class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class AddMedHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

class AddRecommendationForm(forms.ModelForm):

    class Meta:
        model = Recommendation
        fields = '__all__'

class AddVisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'