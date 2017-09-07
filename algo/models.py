from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AlgoInfo(models.Model):
    name = models.CharField(max_length=255)
    signal = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255)
    trade = models.CharField(max_length=255)
