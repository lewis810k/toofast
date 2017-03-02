from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    fast_check = models.CharField(max_length=1, default='0')

    def __str__(self):
        return self.username
