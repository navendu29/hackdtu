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

    def __str__(self):
        return self.name

class Patient(models.Model):
    patientname=models.CharField(max_length=500,default=0)
    patientcontact = models.CharField(max_length=100,default=0)
    symptoms=models.CharField(max_length=5000,default=0)
    dp=models.CharField(max_length=200,default=0)
    password=models.CharField(max_length=500,default=0)

    def __str__(self):
          return self.patientcontact+'-'+self.patientname

class Disease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease=models.CharField(max_length=500)
    prescription=models.CharField(max_length=100000)

    def __str__(self):
        return self.disease





class pharmacist(models.Model):
    pharmacistname = models.CharField(max_length=500)
    dp = models.CharField(max_length=200)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.pharmacistnasme
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)