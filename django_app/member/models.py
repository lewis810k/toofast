from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    name = models.CharField(max_length=5)
    git_url = models.URLField(blank=True)
    phone_number = models.CharField(max_length=15,blank=True)
    git_service = models.BooleanField(default=False)
    fast_check = models.ForeignKey(
        'FastCheck',
        null=True,
        blank=True,
        related_name='fast_check_users'
    )

    def __str__(self):
        return self.username


class FastCheck(models.Model):
    click = models.CharField(max_length=1, default='0')
