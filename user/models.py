from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images',null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)

# Create your models here.
