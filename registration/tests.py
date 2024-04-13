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

# @pytest.mark.django_db
# def test_add_patient():
#     client = Client()
#     url = reverse('patient')
#     response = client.get(url)
#     assert response.status_code == 200

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

@pytest.mark.django_db
def test_add_not_empty_med_history(user):
    client = Client()
    url = reverse('reason')
    data = {
        'interview': 'test',
        'ophthalmological_interview': 'test',
        'visus_distance': 'test',
        'visus_near': 'test',
        'tonus': 'test',
        'anterior_segment_right_eye': 'test',
        'anterior_segment_left_eye': 'test',
        'fundus_segment_right_eye': 'test',
        'fundus_left_eye': 'test',
        'date': '2024-12-10',
        'patient': ''
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('home'))
    assert ReasonForVisit.objects.get(reasons='L12')
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
# def test_add_visit():
#     client = Client()
#     url = reverse('visit')
#     response = client.get(url)
#     assert response.status_code == 200
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





