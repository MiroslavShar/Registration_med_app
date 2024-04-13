import pytest
from registration.models import Doctor, Patient, MedicalHistory, Recommendation, ReasonForVisit, Visit, User

@pytest.fixture
def doctors():
    doctors = []
    for x in range(5):
        doctors.append(Doctor.objects.create(name=x))
        return doctors

@pytest.fixture
def user():
    u = User.objects.create_user(username='test5', password='test5')
    return u

@pytest.fixture
def reasons():
    reasons = []
    for x in range(7):
        reasons.append(ReasonForVisit.objects.create(reasons=x))
        return reasons

@pytest.fixture
def patients():
    patients = []
    for x in range(7):
        patients.append(Patient.objects.create(name=x, surname=x))
        return patients


@pytest.fixture
def recommendations(patients, new_visit_date='2024-12-10 16:00'):
    recommendations = []
    for x in range(7):
        recommendations.append(Recommendation.objects.create(recommendations=x, patient=patients[x], new_visit_date=new_visit_date))
        return recommendations

@pytest.fixture
def visits(patients, doctors, reasons, date="2024-12-10 16:00"):
    visits = []
    for x in range(7):
        v = Visit.objects.create(patient=patients[x], date=date, reason=reasons[x])
        v.doctor.set(doctors)
        visits.append(v)
        return visits

