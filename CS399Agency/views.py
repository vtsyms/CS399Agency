
from django.shortcuts import render


def index(request):
  	return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contests(request):
    return render(request, 'contests.html')

def connect(request):
    return render(request, 'connect.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    return render(request, 'signup.html')

def friend(request):
    return render(request, 'friend.html')

def campaigns(request):
    return render(request, 'campaigns.html')

def campone(request):
    return render(request, 'campone.html')

def camptwo(request):
    return render(request, 'camptwo.html')

def campthree(request):
    return render(request, 'campthree.html')