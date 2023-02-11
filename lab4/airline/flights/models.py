from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_lenght=64)
    destination = models.CharField(max_lenght=64)
    duration = models.IntegerField()