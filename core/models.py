from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    favourite_movies = models.ManyToManyField("movies.Movie")
    avatar = models.ImageField(
        upload_to = 'avatars/', null=True, blank=True
    )