from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from patients.models import Patient
from .models import User
from doctors.models import Doctors
from django import forms

class PatientSignUpForm(UserCreationForm):
    full_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.CharField(required=True)
    email= forms.EmailField(required=True)
    address= forms.CharField()
    phone = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.pname = self.cleaned_data.get('full_name')
        patient.age = self.cleaned_data.get('age')
        patient.gender = self.cleaned_data.get('gender')
        patient.email = self.cleaned_data.get('email')
        patient.address = self.cleaned_data.get('address')
        patient.phone = self.cleaned_data.get('phone')
        patient.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    ROLE = (
			('Doctor', 'Doctor'),
			('Staff', 'Staff'),
			
			)
    full_name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE)
    specialisation = forms.CharField(required=True)
    address = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_staff - True
        user.save()
        doctor = Doctors.objects.create(user=user)
        doctor.dname = self.cleaned_data.get('full_name')
        doctor.phone = self.cleaned_data.get('phone')
        doctor.email = self.cleaned_data.get('email')
        doctor.role = self.cleaned_data.get('role')
        doctor.specialisation = self.cleaned_data.get('specialisation')
        doctor.address = self.cleaned_data.get('address')
        doctor.save()
        return user