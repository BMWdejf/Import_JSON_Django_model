from django.db import models

# Create your models here.
class Adresar(models.Model):
    kod = models.CharField(max_length=100)
    nazev = models.CharField(max_length=100)