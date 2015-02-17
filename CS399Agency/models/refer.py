from django.db import models

class Refer(models.Model):
    email = models.EmailField(max_length=254)
    fEmail = models.EmailField(max_length=254)
    fFirstName = models.CharField(max_length=128, default="")
    fLastName = models.CharField(max_length=128, default="")
    created = models.DateTimeField(auto_now_add=True)

