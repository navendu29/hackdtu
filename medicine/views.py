from django.shortcuts import render

# Create your views here.

from .models import Doctor,Disease
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View

def doc(request):
    doctor_list=Doctor.objects.all()
    if len(doctor_list)==0:
        raise Http404("No Doctors Found")
    return render(request,'medicine/front.html',{'doctor_list':doctor_list})

