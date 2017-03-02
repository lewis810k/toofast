from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    name = models.CharField(max_length=5)
    git_url = models.URLField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    git_service = models.BooleanField(default=False)
    fast_check = models.CharField(max_length=1, default='0')

    def __str__(self):
        return self.username
