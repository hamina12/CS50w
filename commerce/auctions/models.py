from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Aunction(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=, decimal_places=2)
    pic = models.ImageField()

    def __str__(self):
        return f"{self.name}: {self.price}"

class Bid(models.Model):
    aunction = models.ForeignKey(Aunction, on_delete=models.CASCADE, related_name="item")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="lastbid")
    current = models.DecimalField(max_digits=None, decimal_places=2)

    def __str__(self):
        return f"{self.item}: {self.user}|{self.current}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    aunction = models.ForeignKey(Aunction, on_delete=models.CASCADE, related_name="onitem")
    comment = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.item}|{self.user}: {self.comment}"


