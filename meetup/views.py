from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

first_time = True

# Create your views here.
def homeView(request):
  HttpResponse('Hello, this is homeView')