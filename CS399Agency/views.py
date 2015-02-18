from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from models import Signup


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

class SignupForm(forms.Form):
    firstName = forms.CharField(label = "First Name")
    lastName = forms.CharField(label = "Last Name")
    email = forms.EmailField(label = "Your Email")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            su = Signup()
            su.firstName = form.cleaned_data["firstName"]
            su.lastName = form.cleaned_data["lastName"]
            su.email = form.cleaned_data["email"]
            su.save()
            return HttpResponseRedirect ("/ts/")

    elif request.method == 'GET':
            form = SignupForm()
    else:
        return HttpResponseRedirect ("/404/")
    return render(request, "signup.html", {"form": form})

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

def ts(request):
    return render(request, 'ts.html')