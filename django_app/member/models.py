from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    name = models.CharField(max_length=5)
    fast_check = models.CharField(max_length=1, default='0')
    git_url = models.URLField()
    phone_number = models.CharField(max_length=15)
    git_service = models.BooleanField(default=False)

    def __str__(self):
        return self.username
