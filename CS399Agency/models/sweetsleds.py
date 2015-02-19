from django.db import models

class SweetSleds(models.Model):
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)