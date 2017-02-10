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
