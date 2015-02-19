from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from models import Signup, Contest, Entrant, Refer


def index(request):
  	return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    
class EntrantForm(forms.Form):
  name = forms.CharField(label="Name")
  email = forms.EmailField(label = "Email")

def contests(request):
  if request.method == 'POST':
    form = EntrantForm(request.POST)
    if form.is_valid():
      en = Entrant()
      en.name = form.cleaned_data["name"]
      en.email = form.cleaned_data["email"]
      en.save()
    return HttpResponseRedirect ("/ts/")
  elif request.method == 'GET':
    form = EntrantForm()
  else:
    return HttpResponseRedirect("/404/")
  return render(request, 'contests.html', {"form": form, "contests": Contest.objects.order_by("deadline")})

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

class ReferForm(forms.Form):
    yourEmail = forms.EmailField(label = "Your Email")
    friendsEmail = forms.EmailField(label = "Friends Email")
    friendsFirstName = forms.CharField(label = "Friends First Name")
    friendsLastName = forms.CharField(label = "Friends Last Name")

def friend(request):
    if request.method == 'POST':
        form = ReferForm(request.POST)
        if form.is_valid():
            refer = Refer()
            refer.yourEmail = form.cleaned_data["yourEmail"]
            refer.friendsEmail = form.cleaned_data["friendsEmail"]
            refer.friendsFirstName = form.cleaned_data["friendsFirstName"]
            refer.friendsLastName = form.cleaned_data["friendsLastName"]
            refer.save()
            return HttpResponseRedirect ("/reffered/")
    elif request.method == 'GET':
        form = ReferForm()
    else:
        return HttpResponseRedirect ("/404/")
    return render(request, 'friend.html', {"form": form})

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

def reffered(request):
    return render(request, 'reffered.html')

def error(request):
    return render(request, '404.html')
