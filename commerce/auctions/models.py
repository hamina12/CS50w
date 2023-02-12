from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Aunction(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    pic = models.ImageField()

    def __str__(self):
        return f"{self.name}: {self.price}"


