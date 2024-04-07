from django.shortcuts import render, redirect
from django.views import View
from registration.models import Doctor, MedicalHistory, Recommendation, ReasonForVisit, Patient, Visit
from django.http import HttpResponse
from registration.forms import ReasonForm, AddDoctorForm, AddPatientForm, AddMedHistoryForm, AddRecommendationForm, AddVisitForm

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

class AddMedicalHistory(View):
    def get(self, request):
        form = AddMedHistoryForm
        return render(request, 'add_med_history.html', {'form': form})

    def post(self, request):
        form = AddMedHistoryForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('home')
        return render(request, 'add_med_history.html', {'form': form})

class AddRecommendation(View):
    def get(self, request):
        form = AddRecommendationForm
        return render(request, 'add_recommendation.html', {'form': form})

    def post(self, request):
        form = AddRecommendationForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('home')
        return render(request, 'add_recommendation.html', {'form': form})

class AddVisit(View):
    def get(self, request):
        form = AddVisitForm
        return render(request, 'add_visit.html', {'form': form})

    def post(self, request):
        form = AddVisitForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('home')
        return render(request, 'add_visit.html', {'form': form})

class LetSeeDoctor(View):
    def get(self, request):
        db_doctors = Doctor.objects.all()
        return render(request, 'show_doctors.html', {'doctors': db_doctors})

class LetEditDoctor(View):
    def get(self, request, id):
        doctor = Doctor.objects.get(pk=id)
        form = AddDoctorForm(instance=doctor)
        return render(request, 'add_doctor.html', {'form': form})
    def post(self, request, id):
        dostor = Doctor.objects.get(pk=id)
        form = AddDoctorForm(request.POST, instance=dostor)
        if form.is_valid():
            form.save()
            return redirect('show_doctors')
        return render(request, 'add_doctor.html', {'form': form})

