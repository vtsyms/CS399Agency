
from django.shortcuts import render


def index(request):
  	return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contests(request):
    return render(request, 'contests.html')

def connect(request):
    return render(request, 'connect.html')
