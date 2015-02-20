from django.db import models

class Smartpets(models.Model):
    email = models.EmailField(max_length=254)