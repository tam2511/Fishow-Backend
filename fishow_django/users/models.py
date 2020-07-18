from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    rating = models.IntegerField(default=0)
    count_blogs = models.IntegerField(default=0)
    count_comments = models.IntegerField(default=0)

