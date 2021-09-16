# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Patient(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)

    man = 'Man'
    woman = 'Woman'
    other = 'Other'
    sexes = [(man, man), (woman, woman), (other, other)]

    sex = models.TextField('Sex', choices=sexes)
    age = models.IntegerField('Age')

    height = models.IntegerField('Height (in centimeters)', validators=[
            MaxValueValidator(300),
            MinValueValidator(1)])
    weight = models.IntegerField('Weight (in kilogrammes)', validators=[
            MaxValueValidator(500),
            MinValueValidator(1)])

    proper_signal = models.FileField("Proper signal", upload_to='uploads/signals/')
    antagonist_signal = models.FileField("Antagonist signal", upload_to='uploads/signals/')
    hold_signal = models.FileField("Hold signal", upload_to='uploads/signals/')

    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('patient_edit', kwargs={'pk': self.pk})
