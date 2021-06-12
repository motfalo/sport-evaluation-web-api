# -*- coding: utf-8 -*-
from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    average_emg = models.DecimalField('Average EMG value', decimal_places=2, max_digits=8)
    max_emg = models.DecimalField('Maximal EMG value', decimal_places=2, max_digits=8)
    min_emg = models.DecimalField('Minimal EMG value', decimal_places=2, max_digits=8)
    # price = models.DecimalField('Price', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
