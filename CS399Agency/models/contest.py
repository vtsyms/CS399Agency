from django.db import models

class Contest(models.Model):
    name = models.CharField(max_length=128, default="")
    deadline = models.DateField()
    description = models.TextField()
    
class Entrant(models.Model):
  name = models.CharField(max_length=128, default="")
  email = models.EmailField(max_length=254)