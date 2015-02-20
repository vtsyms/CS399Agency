from django.db import models

class Logos(models.Model):
	name = models.CharField(max_length=128,default="")
	email = models.EmailField(max_length=255, default="")