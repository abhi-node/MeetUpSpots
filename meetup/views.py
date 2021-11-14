from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

first_time = True

# Create your views here.
def homeView(request):
  return render(request, "index.html")
def meetView(request):
  return render(request, "meetup.html")