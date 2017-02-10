from __future__ import unicode_literals

from django.db import models


from django.core.urlresolvers import reverse

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    degree=models.CharField(max_length=20)
    designation=models.CharField(max_length=30)
    doctor_dp=models.CharField(max_length=500)
    contactno=models.CharField(max_length=10)
    specialisation=models.CharField(max_length=40)
    workplace=models.CharField(max_length=100)
    password=models.CharField(max_length=300,default=None)
class Disease(models.Model):
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease=models.CharField(max_length=500)
    prescription=models.CharField(max_length=100000)