from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Auction(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=64, decimal_places=2)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return f"{self.id}{self.name}: {self.price}"

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="item", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lastbid")
    current = models.DecimalField(max_digits=64, decimal_places=2)

    def __str__(self):
        return f"{self.item}: {self.user}|{self.current}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="onitem")
    comment = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.item}|{self.user}: {self.comment}"




