# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PatientList.as_view(), name='patient_list'),
    path('view/<int:pk>', views.PatientDetail.as_view(), name='patient_view'),
    path('proper/<int:pk>', views.PatientProper.as_view(), name='patient_proper'),
    path('antagonist/<int:pk>', views.PatientAntagonist.as_view(), name='patient_antagonist'),
    path('hold/<int:pk>', views.PatientHold.as_view(), name='patient_hold'),
    path('new', views.PatientCreate.as_view(), name='patient_new'),
    path('edit/<int:pk>', views.PatientUpdate.as_view(), name='patient_edit'),
    path('delete/<int:pk>', views.PatientDelete.as_view(), name='patient_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)