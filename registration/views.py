from django.shortcuts import render, redirect
from django.views import View
from registration.models import Doctor, MedicalHistory, Recommendation, ReasonForVisit, Patient, Visit
from django.http import HttpResponse
from registration.forms import ReasonForm, AddDoctorForm, AddPatientForm

class IndexPage(View):
    def get(self, request):
        return redirect('home')

class AddDoctor(View):
    def get(self, request):
        form = AddDoctorForm
        return render(request, 'add_doctor.html', {'form': form})
    def post(self, request):
        form = AddDoctorForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('home')
        return render(request, 'add_doctor.html', {'form': form})

class AddReason(View):
    def get(self, request):
        form = ReasonForm
        return render(request, 'add_reason.html', {'form': form})
    def post(self, request):
        form = ReasonForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('home')
        return render(request, 'add_reason.html', {'form': form})

class AddPatient(View):
    def get(self, request):
        form = AddPatientForm
        return render(request, 'add_patient.html', {'form': form})
    def post(self, request):
        form = AddPatientForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('home')
        return render(request, 'add_patient.html', {'form': form})