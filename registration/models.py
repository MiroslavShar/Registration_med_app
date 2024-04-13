from django.db import models
from django.contrib.auth.models import User, Group, Permission

class Doctor(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Patient(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    # medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'

class MedicalHistory(models.Model):
    interview = models.CharField(max_length=510)
    ophthalmological_interview = models.CharField(max_length=510)
    visus_distance = models.CharField(max_length=255, null=True)
    visus_near = models.CharField(max_length=255, null=True)
    tonus = models.CharField(max_length=255, null=True)
    anterior_segment_right_eye = models.CharField(max_length=255)
    anterior_segment_left_eye = models.CharField(max_length=255)
    fundus_segment_right_eye = models.CharField(max_length=255)
    fundus_left_eye = models.CharField(max_length=255)
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Recommendation(models.Model):
    recommendations = models.CharField(max_length=64)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    new_visit_date = models.DateTimeField()

    def __str__(self):
        return f'{self.recommendations} {self.patient} {self.new_visit_date}'


class ReasonForVisit(models.Model):
    reasons = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.reasons}'



class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ManyToManyField(Doctor)
    date = models.DateTimeField()
    reason = models.ForeignKey(ReasonForVisit, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient} {self.doctor} {self.date} {self.reason}'