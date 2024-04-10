from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from registration.models import Doctor, MedicalHistory, Recommendation, ReasonForVisit, Patient, Visit
from django.http import HttpResponse
from registration.forms import ReasonForm, AddDoctorForm, AddPatientForm, AddMedHistoryForm, AddRecommendationForm, AddVisitForm, VisitSearchForm, PatientSearch

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

class LetSeeReason(View):
    def get(self, request):
        db_reason = ReasonForVisit.objects.all()
        return render(request, 'show_reasons.html', {'reasons': db_reason})

class LetEditReason(View):
    def get(self, request, id):
        reason = ReasonForVisit.objects.get(pk=id)
        form = ReasonForm(instance=reason)
        return render(request, 'add_reason.html', {'form': form})

    def post(self, request, id):
        reason = ReasonForVisit.objects.get(pk=id)
        form = ReasonForm(request.POST, instance=reason)
        if form.is_valid():
            form.save()
            return redirect('show_reasons')
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

class LetShowPatients(View):
    def get(self, request):
        db_patient = Patient.objects.all()
        form = PatientSearch(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            db_patient = db_patient.filter(name__contains=name)
            surname = form.cleaned_data.get('surname', '')
            if surname:
                db_patient = db_patient.filter(surname__contains=surname)
        return render(request, 'show_patient.html', {'patients': db_patient, 'form': form})

class LetDeletePatient(View):

    def get(self, request, id):
        patient = Patient.objects.get(pk=id)
        form = AddPatientForm(instance=patient)
        return render(request, 'delete_patient.html', {'form': form})
    def post(self, request, id):
        db_patient = Patient.objects.get(pk=id)
        form = AddPatientForm(request.POST, instance=db_patient)
        if form.is_valid():
            db_patient.delete()
            return redirect('show_patients')
        return redirect('show_patients')



class LetEditPatient(View):
    def get(self, request, id):
        patient = Patient.objects.get(pk=id)
        form = AddPatientForm(instance=patient)
        return render(request, 'add_patient.html', {'form': form})

    def post(self, request, id):
        patient = Patient.objects.get(pk=id)
        form = AddPatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('show_patients')
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

class LetShowHistory(View):
    def get(self, request):
        db_history = MedicalHistory.objects.all()
        return render(request, 'show_history.html', {'histories': db_history})

class LetEditHistory(View):
    def get(self, request, id):
        history = MedicalHistory.objects.get(pk=id)
        form = AddMedHistoryForm(instance=history)
        return render(request, 'add_med_history.html', {'form': form})

    def post(self, request, id):
        history = MedicalHistory.objects.get(pk=id)
        form = AddMedHistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('show_histories')
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

class LetShowRecommendation(View):
    def get(self, request):
        db_recommendation = Recommendation.objects.all()
        return render(request, 'show_recommendation.html', {'recommendations': db_recommendation})

class LetEditRecommendation(View):
    def get(self, request, id):
        recommendation = Recommendation.objects.get(pk=id)
        form = AddRecommendationForm(instance=recommendation)
        return render(request, 'add_recommendation.html', {'form': form})

    def post(self, request, id):
        recommendation = Recommendation.objects.get(pk=id)
        form = AddRecommendationForm(request.POST, instance=recommendation)
        if form.is_valid():
            form.save()
            return redirect('show_recommendation')
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

class LetShowVisit(View):
    def get(self, request):
        db_visit = Visit.objects.all()
        form = VisitSearchForm(request.GET)
        if form.is_valid():
            patient = form.cleaned_data.get('patient', '')
            db_visit = db_visit.filter(patient__name__icontains=patient)
            doctor = form.cleaned_data.get('doctor')
            if doctor:
                db_visit = db_visit.filter(doctor__name__contains=doctor)
            date = form.cleaned_data.get('date')
            if date:
                db_visit = db_visit.filter(date=date)
            reason = form.cleaned_data.get('reason')
            for r in reason:
                db_visit = db_visit.filter(reason=r)
        return render(request, 'show_visit.html', {'visits': db_visit, 'form': form})

class LetEditVisit(View):
    def get(self, request, id):
        visit = Visit.objects.get(pk=id)
        form = AddVisitForm(instance=visit)
        return render(request, 'add_visit.html', {'form': form})

    def post(self, request, id):
        visit = Visit.objects.get(pk=id)
        form = AddVisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('show_visit')
        return render(request, 'add_visit.html', {'visits': visit})



