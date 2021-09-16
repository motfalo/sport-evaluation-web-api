# -*- coding: utf-8 -*-
from django import forms

from .models import Patient

class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['proper_signal'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['antagonist_signal'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['hold_signal'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Patient
        fields = "__all__"
        # fields = ('name', 'description', 'proper_signal', 'antagonist_signal', 'hold_signal')