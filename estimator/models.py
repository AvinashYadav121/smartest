from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', default='default.jpg')

    def __str__(self):
        return self.username
