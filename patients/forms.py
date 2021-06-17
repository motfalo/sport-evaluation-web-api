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
        self.fields['average_emg_proper_muscle'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['average_emg_antagonist_muscle'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['average_emg_hold_muscle'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        # self.fields['max_emg_proper_muscle'].widget.attrs = {
        #     'class': 'form-control col-md-6',
        #     'step': 'any',
        #     'min': '1',
        # }
        # self.fields['max_emg_antagonist_muscle'].widget.attrs = {
        #     'class': 'form-control col-md-6',
        #     'step': 'any',
        #     'min': '1',
        # }
        # self.fields['max_emg_hold_muscle'].widget.attrs = {
        #     'class': 'form-control col-md-6',
        #     'step': 'any',
        #     'min': '1',
        # }
        # self.fields['min_emg_proper_muscle'].widget.attrs = {
        #     'class': 'form-control col-md-6',
        #     'step': 'any',
        #     'min': '1',
        # }
        # self.fields['min_emg_antagonist_muscle'].widget.attrs = {
        #     'class': 'form-control col-md-6',
        #     'step': 'any',
        #     'min': '1',
        # }
        # self.fields['min_emg_hold_muscle'].widget.attrs = {
        #     'class': 'form-control col-md-6',
        #     'step': 'any',
        #     'min': '1',
        # }

    class Meta:
        model = Patient
        fields = ('name', 'description', 'average_emg_proper_muscle', 'average_emg_antagonist_muscle', 'average_emg_hold_muscle', 'max_emg_proper_muscle', 'max_emg_antagonist_muscle', 'max_emg_hold_muscle', 'min_emg_proper_muscle', 'min_emg_antagonist_muscle', 'min_emg_hold_muscle')