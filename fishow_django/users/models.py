from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    social_rating = models.IntegerField(default=0)
    fishing_rating = models.IntegerField(default=0)
    views_blogs = models.IntegerField(default=0)
    view_reports = models.IntegerField(default=0)
    views_profile = models.IntegerField(default=0)
    count_blogs = models.IntegerField(default=0)
    count_comments = models.IntegerField(default=0)

