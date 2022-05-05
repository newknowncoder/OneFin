from django.contrib.auth.models import AbstractUser
from django.db import models

#create user model
class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []