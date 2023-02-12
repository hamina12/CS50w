from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class aunctions(models.Model):
    name = models.CharField(max_length=64)
    prize = model.AutoField


