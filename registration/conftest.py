import pytest
from registration.models import Doctor, Patient, MedicalHistory, Recommendation, ReasonForVisit, Visit

@pytest.fixture
def doctors():
    doctors = []
    for x in range(5):
        doctors.append(Doctor.objects.create(name=x))
        return doctors