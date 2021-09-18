# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from patients.functions import signal_processing as sp
from django.core.files.storage import FileSystemStorage
from .models import Patient
from .forms import PatientForm

class PatientList(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'


class PatientDetail(DetailView):
    model = Patient
    template_name = 'patients/patient_detail.html'


class PatientProper(DetailView):
    model = Patient
    template_name = 'patients/patient_proper.html'


class PatientAntagonist(DetailView):
    model = Patient
    template_name = 'patients/patient_antagonist.html'


class PatientHold(DetailView):
    model = Patient
    template_name = 'patients/patient_hold.html'


class PatientCreate(SuccessMessageMixin, CreateView):
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('patient_list')
    success_message = "Patient successfully created!"


class PatientUpdate(SuccessMessageMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('patient_list')
    success_message = "Patient successfully updated!"


class PatientDelete(SuccessMessageMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')
    success_message = "Patient successfully deleted!"
