from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)