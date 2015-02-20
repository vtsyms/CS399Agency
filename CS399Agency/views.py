from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from models import Signup, Contest, Entrant, Refer, Contact, Sweetsleds


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

class ContactForm(forms.Form):
    email = forms.EmailField(label = "Your Email")
    firstName = forms.CharField(label = "Your First Name")
    lastName = forms.CharField(label = "Your Last Name")
    subject = forms.CharField(label = "Your Subject")
    message = forms.CharField(label = "Your Message")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            co = Contact()
            co.email = form.cleaned_data["email"]
            co.firstName = form.cleaned_data["firstName"]
            co.lastName = form.cleaned_data["lastName"]
            co.subject = form.cleaned_data["subject"]
            co.message = form.cleaned_data["message"]
            co.save()
            return HttpResponseRedirect ("/feedback/")
    elif request.method == 'GET':
        form = ContactForm()
    else:
        return HttpResponseRedirect ("/404/")
    return render(request, 'contact.html', {"form": form})

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

class SweetSledsForm(forms.Form):
    email = forms.EmailField(label = "Your Email")

def campone(request):
    if request.method == 'POST':
        form = SweetSledsForm(request.POST)
        if form.is_valid():
            ss = Sweetsleds()
            ss.email = form.cleaned_data["email"]
            ss.save()
            return HttpResponseRedirect ("/ts/")

    elif request.method == 'GET':
            form = SweetSledsForm()
    else:
        return HttpResponseRedirect ("/404/")
    return render(request, "campone.html", {"form": form})

class ReferForm(forms.Form):
    email = forms.EmailField(label = "Your Email")
    fEmail = forms.EmailField(label = "Friends Email")
    fFirstName = forms.CharField(label = "Friends First Name")
    fLastName = forms.CharField(label = "Friends Last Name")

def friend(request):
    if request.method == 'POST':
        form = ReferForm(request.POST)
        if form.is_valid():
            refer = Refer()
            refer.email = form.cleaned_data["email"]
            refer.fEmail = form.cleaned_data["fEmail"]
            refer.fFirstName = form.cleaned_data["fFirstName"]
            refer.fLastName = form.cleaned_data["fLastName"]
            refer.save()
            return HttpResponseRedirect ("/reffered/")
    elif request.method == 'GET':
        form = ReferForm()
    else:
        return HttpResponseRedirect ("/404/")
    return render(request, 'friend.html', {"form": form})

def campaigns(request):
    return render(request, 'campaigns.html')

def camptwo(request):
    return render(request, 'camptwo.html')

def campthree(request):
    return render(request, 'campthree.html')

def ts(request):
    return render(request, 'ts.html')

def reffered(request):
    return render(request, 'reffered.html')

def feedback(request):
    return render(request, 'feedback.html')

def error(request):
    return render(request, '404.html')
