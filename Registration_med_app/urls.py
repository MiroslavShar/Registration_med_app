"""
URL configuration for Registration_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('add_doctor/', views.AddDoctor.as_view(), name='doctor'),
    path('add_reason/', views.AddReason.as_view(), name='reason'),
    path('add_patient/', views.AddPatient.as_view(), name='patient'),
    path('add_med_history/', views.AddMedicalHistory.as_view(), name='history'),
    path('add_recommendation/', views.AddRecommendation.as_view(), name='recommendation'),
    path('add_visit/', views.AddVisit.as_view(), name='visit'),
    path('show_doctors/', views.LetSeeDoctor.as_view(), name='show_doctors'),
    path('show_doctors/<int:id>/', views.LetEditDoctor.as_view(), name='edit_doctor'),
    path('show_reasons/', views.LetSeeReason.as_view(), name='show_reasons'),
    path('show_reasons/<int:id>/', views.LetEditReason.as_view(), name='edit_reasons'),
    path('show_patient/', views.LetShowPatients.as_view(), name='show_patients'),
    path('show_patient/<int:id>/', views.LetEditPatient.as_view(), name='edit_patient'),
    path('show_histories/', views.LetShowHistory.as_view(), name='show_histories'),
    path('show_histories/<int:id>', views.LetEditHistory.as_view(), name='edit_history'),

]