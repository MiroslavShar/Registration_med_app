from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    # medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)

class MedicalHistory(models.Model):
    interview = models.CharField(max_length=510)
    ophthalmological_interview = models.CharField(max_length=510)
    visus_distance = models.IntegerField
    visus_near = models.IntegerField
    tonus = models.IntegerField
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


class ReasonForVisit(models.Model):
    reasons = models.CharField(max_length=64)



class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.ForeignKey(ReasonForVisit, on_delete=models.CASCADE)