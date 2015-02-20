from django.db import models

class Sweetsleds(models.Model):
    email = models.EmailField(max_length=254)