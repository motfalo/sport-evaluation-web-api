# -*- coding: utf-8 -*-
from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    average_emg_proper_muscle = models.DecimalField('Average proper muscle EMG', decimal_places=2, max_digits=8)
    average_emg_antagonist_muscle = models.DecimalField('Average antagonist muscle EMG', decimal_places=2, max_digits=8)
    average_emg_wrong_muscle = models.DecimalField('Average wrong muscle EMG', decimal_places=2, max_digits=8)
    max_emg_proper_muscle = models.DecimalField('Maximal proper muscle EMG', decimal_places=2, max_digits=8)
    max_emg_antagonist_muscle = models.DecimalField('Maximal antagonist muscle EMG', decimal_places=2, max_digits=8)
    max_emg_wrong_muscle = models.DecimalField('Maximal wrong muscle EMG', decimal_places=2, max_digits=8)
    min_emg_proper_muscle = models.DecimalField('Minimal proper muscle EMG', decimal_places=2, max_digits=8)
    min_emg_antagonist_muscle = models.DecimalField('Minimal antagonist muscle EMG', decimal_places=2, max_digits=8)
    min_emg_wrong_muscle = models.DecimalField('Minimal wrong muscle EMG', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
