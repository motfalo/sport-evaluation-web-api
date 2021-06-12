# -*- coding: utf-8 -*-
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['average_emg'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['max_emg'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['min_emg'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Product
        fields = ('name', 'description', 'average_emg', 'max_emg', 'min_emg')