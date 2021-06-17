# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Patient
from .forms import PatientForm

class PatientList(ListView):
    model = Patient

class PatientDetail(DetailView):
    model = Patient

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


