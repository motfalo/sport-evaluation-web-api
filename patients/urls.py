# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientList.as_view(), name='patient_list'),
    path('view/<int:pk>', views.PatientDetail.as_view(), name='patient_view'),
    path('new', views.PatientCreate.as_view(), name='patient_new'),
    path('edit/<int:pk>', views.PatientUpdate.as_view(), name='patient_edit'),
    path('delete/<int:pk>', views.PatientDelete.as_view(), name='patient_delete'),
]