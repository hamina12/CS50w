from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Aunction(models.Model):
    name = models.CharField(max_length=64)
    prize = models.IntegerField()
    pic = models.ImageField()


