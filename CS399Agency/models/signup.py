from django.db import models

class Signup(models.Model):
    firstName = models.CharField(max_length=128, default="")
    lastName = models.CharField(max_length=128, default="")
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
