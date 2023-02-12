from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Aunction(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField(min_lenght=0)
    pic = models.ImageField()

    def __str__(self):
        return f"{self.name}: {self.price}"

class Bid(models.Model):
    item = models.ForeignKey(Aunction, on_delete=models.CASCADE, relate_name="item")
    current = models.IntegerField(min_lenght=0)

    def __str__(self):
        return f"{self.item} :{self.current}"

class Comment(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Aunction, on_delete=models.CASCADE, relate_name="item")
    comment = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.item}|{self.user}: {self.comment}"


