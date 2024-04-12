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
#     Doctor.objects.get(name='Aleksander')

@pytest.mark.django_db
def test_let_see_doctor(doctors):
    client = Client()
    url = reverse('show_doctors')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['doctors'].count() == len(doctors)