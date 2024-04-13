from django.test import TestCase, Client
from django.urls import reverse
from registration.models import Doctor, Patient, MedicalHistory, Recommendation, ReasonForVisit, Visit
import pytest

# def test_home_view():
#     client = Client()
#     url = reverse('home')
#     response = client.get(url)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_doctor():
#     client = Client()
#     url = reverse('doctor')
#     response = client.get(url)
#     assert response.status_code == 200
#
#
# @pytest.mark.django_db
# def test_add_empty_doctor():
#     client = Client()
#     url = reverse('doctor')
#     data = {
#         'name': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_empty_doctor_2():
#     client = Client()
#     url = reverse('doctor')
#     data = {
#         'name': '',
#         'surname': 'Schubert',
#         'specialization': 'Neirosurgery'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_doctor_2():
#     client = Client()
#     url = reverse('doctor')
#     data = {
#         'name': 'Aleksander',
#         'surname': 'Schubert',
#         'specialization': 'Neirosurgery'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('home'))
#     assert Doctor.objects.get(name='Aleksander')
#
#
# @pytest.mark.django_db
# def test_let_see_doctor(doctors):
#     client = Client()
#     url = reverse('show_doctors')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['doctors'].count() == len(doctors)
#
# @pytest.mark.django_db
# def test_add_reason():
#     client = Client()
#     url = reverse('reason')
#     response = client.get(url)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_empty_reason():
#     client = Client()
#     url = reverse('reason')
#     data = {
#         'reasons': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_not_empty_reason():
#     client = Client()
#     url = reverse('reason')
#     data = {
#         'reasons': 'L12'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('home'))
#     assert ReasonForVisit.objects.get(reasons='L12')
#
# @pytest.mark.django_db
# def test_add_patient():
#     client = Client()
#     url = reverse('patient')
#     response = client.get(url)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_empty_patient():
#     client = Client()
#     url = reverse('patient')
#     data = {
#         'name': '',
#         'surname': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_not_empty_patient():
#     client = Client()
#     url = reverse('patient')
#     data = {
#         'name': 'Ludovico',
#         'surname': 'Wielki'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('home'))
#     assert Patient.objects.get(name='Ludovico', surname='Wielki')
#
# @pytest.mark.django_db
# def test_not_login_add_med_history():
#     client = Client()
#     url = reverse('history')
#     response = client.get(url)
#     assert response.status_code == 302 #Musisz być zalogowany
#
# @pytest.mark.django_db
# def test_login_add_med_history(user):
#     client = Client()
#     client.force_login(user)
#     url = reverse('history')
#     response = client.get(url)
#     assert response.status_code == 200 #Musisz być zalogowany
#
# @pytest.mark.django_db
# def test_add_empty_med_history(user):
#     client = Client()
#     client.force_login(user)
#     url = reverse('history')
#     data = {
#         'interview': '',
#         'ophthalmological_interview': '',
#         'visus_distance': '',
#         'visus_near': '',
#         'tonus': '',
#         'anterior_segment_right_eye': '',
#         'anterior_segment_left_eye': '',
#         'fundus_segment_right_eye': '',
#         'fundus_left_eye': '',
#         'date': '',
#         'patient': '',
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_not_empty_med_history(user, patients):
#     client = Client()
#     client.force_login(user)
#     url = reverse('history')
#     data = {
#         'interview': 'test',
#         'ophthalmological_interview': 'test',
#         'visus_distance': 'test',
#         'visus_near': 'test',
#         'tonus': 'test',
#         'anterior_segment_right_eye': 'test',
#         'anterior_segment_left_eye': 'test',
#         'fundus_segment_right_eye': 'test',
#         'fundus_left_eye': 'test',
#         'date': '2024-07-05',
#         'patient': f'{patients[0].id}'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('home'))
#     assert MedicalHistory.objects.get(interview="test")
#
# @pytest.mark.django_db
# def test_show_histories():
#     client = Client()
#     url = reverse('show_histories')
#     response = client.get(url)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_recomendation():
#     client = Client()
#     url = reverse('recommendation')
#     response = client.get(url)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_empty_recomendation(user):
#     client = Client()
#     client.force_login(user)
#     url = reverse('recommendation')
#     data = {
#         'recommendations': '',
#         'new_visit_date': '',
#         'patient': '',
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_not_empty_recomendation(user, patients):
#     client = Client()
#     client.force_login(user)
#     url = reverse('recommendation')
#     data = {
#         'recommendations': 'L_Test',
#         'new_visit_date': '2024-12-10 16:00',
#         'patient': f'{patients[0].id}'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('home'))
#     assert Recommendation.objects.get(recommendations='L_Test')
#
# @pytest.mark.django_db
# def test_add_visit():
#     client = Client()
#     url = reverse('visit')
#     response = client.get(url)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_empty_visit(user):
#     client = Client()
#     client.force_login(user)
#     url = reverse('visit')
#     data = {
#         'patient': '',
#         'doctor': '',
#         'date': '',
#         'reason': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_not_empty_visit(user, patients, doctors, reasons):
#     client = Client()
#     client.force_login(user)
#     url = reverse('visit')
#     data = {
#         'doctor': f'{doctors[0].id}',
#         'date': '2024-12-10 16:00',
#         'patient': f'{patients[0].id}',
#         'reason': f'{reasons[0].id}'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('home'))
#     assert Visit.objects.get(doctor=f'{doctors[0].id}')
#
#
#
#
# @pytest.mark.django_db
# def test_show_reason(reasons):
#     client = Client()
#     url = reverse('show_reasons')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['reasons'].count() == len(reasons)
#
# @pytest.mark.django_db
# def test_show_patients(patients):
#     client = Client()
#     url = reverse('show_patients')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['patients'].count() == len(patients)
#
# @pytest.mark.django_db
# def test_show_recommendations(recommendations):
#     client = Client()
#     url = reverse('show_recommendation')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['recommendations'].count() == len(recommendations)
#
# @pytest.mark.django_db
# def test_show_visit(visits):
#     client = Client()
#     url = reverse('show_visit')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['visits'].count() == len(visits)
#
# @pytest.mark.django_db
# def test_edit_empty_doctor(doctors):
#     client = Client()
#     doctor = doctors[0]
#     url = reverse('edit_doctor', args=(doctor.id,))
#     data = {
#         'name': '',
#         'surname': '',
#         'specialization': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_edit_not_empty_doctor(doctors):
#     client = Client()
#     doctor = doctors[0]
#     url = reverse('edit_doctor', args=(doctor.id,))
#     data = {
#         'name': 'Abraam',
#         'surname': 'Lincoln',
#         'specialization': 'Internista'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('show_doctors'))
#     assert Doctor.objects.get(name='Abraam')
#
# @pytest.mark.django_db
# def test_edit_empty_reason(reasons):
#     client = Client()
#     reason = reasons[0]
#     url = reverse('edit_reasons', args=(reason.id,))
#     data = {
#         'reasons': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_edit_not_empty_reason(reasons):
#     client = Client()
#     reason = reasons[0]
#     url = reverse('edit_reasons', args=(reason.id,))
#     data = {
#         'reasons': 'L66'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('show_reasons'))
#     assert ReasonForVisit.objects.get(reasons='L66')
#
#
# @pytest.mark.django_db
# def test_edit_empty_patient(patients):
#     client = Client()
#     patient = patients[0]
#     url = reverse('edit_patient', args=(patient.id,))
#     data = {
#         'name': '',
#         'surname': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_not_empty_patient(patients):
#     client = Client()
#     patient = patients[0]
#     url = reverse('edit_patient', args=(patient.id,))
#     data = {
#         'name': 'Ludovico',
#         'surname': 'Wielki'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('show_patients'))
#     assert Patient.objects.get(name='Ludovico', surname='Wielki')
#
# @pytest.mark.django_db
# def test_edit_empty_med_history(user, histories):
#     client = Client()
#     client.force_login(user)
#     history = histories[0]
#     url = reverse('edit_history', args=(history.id,))
#     data = {
#         'interview': '',
#         'ophthalmological_interview': '',
#         'visus_distance': '',
#         'visus_near': '',
#         'tonus': '',
#         'anterior_segment_right_eye': '',
#         'anterior_segment_left_eye': '',
#         'fundus_segment_right_eye': '',
#         'fundus_left_eye': '',
#         'date': '',
#         'patient': '',
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_not_empty_med_history(user, patients, histories):
#     client = Client()
#     client.force_login(user)
#     history = histories[0]
#     url = reverse('edit_history', args=(history.id,))
#     data = {
#         'interview': 'test',
#         'ophthalmological_interview': 'test',
#         'visus_distance': 'test',
#         'visus_near': 'test',
#         'tonus': 'test',
#         'anterior_segment_right_eye': 'test',
#         'anterior_segment_left_eye': 'test',
#         'fundus_segment_right_eye': 'test',
#         'fundus_left_eye': 'test',
#         'date': '2024-07-05',
#         'patient': f'{patients[0].id}'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('show_histories'))
#     assert MedicalHistory.objects.get(interview="test")
#
# @pytest.mark.django_db
# def test_edit_empty_recomendation(user, recommendations):
#     client = Client()
#     client.force_login(user)
#     recommendation = recommendations[0]
#     url = reverse('edit_recommendation', args=(recommendation.id,))
#     data = {
#         'recommendations': '',
#         'new_visit_date': '',
#         'patient': '',
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_edit_not_empty_recomendation(user, patients, recommendations):
#     client = Client()
#     client.force_login(user)
#     recommendation = recommendations[0]
#     url = reverse('edit_recommendation', args=(recommendation.id,))
#     data = {
#         'recommendations': 'L_Test',
#         'new_visit_date': '2024-12-10 16:00',
#         'patient': f'{patients[0].id}'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('show_recommendation'))
#     assert Recommendation.objects.get(recommendations='L_Test')
#
#
# @pytest.mark.django_db
# def test_edit_empty_visit(user, visits):
#     client = Client()
#     client.force_login(user)
#     visit = visits[0]
#     url = reverse('edit_visit', args=(visit.id,))
#     data = {
#         'patient': '',
#         'doctor': '',
#         'date': '',
#         'reason': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_not_empty_visit(user, patients, doctors, reasons, visits):
#     client = Client()
#     client.force_login(user)
#     visit = visits[0]
#     url = reverse('edit_visit', args=(visit.id,))
#     data = {
#         'doctor': f'{doctors[0].id}',
#         'date': '2024-12-10 16:00',
#         'patient': f'{patients[0].id}',
#         'reason': f'{reasons[0].id}'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('show_visit'))
#     assert Visit.objects.get(doctor=f'{doctors[0].id}')

@pytest.mark.django_db
def test_delete_empty_patient(patients):
    client = Client()
    patient = patients[0]
    url = reverse('delete_patient', args=(patient.id,))
    data = {
        'name': 'Nie ma takiego',
        'surname': ''
    }
    response = client.post(url, data)
    assert response.status_code == 302

@pytest.mark.django_db
def test_delete_not_empty_patient(patients):
    client = Client()
    patient = patients[0]
    url = reverse('delete_patient', args=(patient.id,))
    data = {
        'name': f'{patients[0].name}',
        'surname': f'{patients[0].surname}'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('show_patients'))
    # assert Patient.objects.get(name='Ludovico', surname='Wielki')

