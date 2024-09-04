from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=200)
    profile_img = ResizedImageField(
        size=[500, 300], upload_to="profile", blank=True,
        null=True, default="/default/default_profile.jpg")
