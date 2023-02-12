from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    aunction_listings = models.CharField(max_lenght=64)
    bids = models.

