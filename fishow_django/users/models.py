from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    country = models.TextField(null=True)
    city = models.TextField(null=True)
    avatar = models.TextField(null=True)
    about = models.TextField(null=True)
    tags = models.TextField(null=True)
    achievement = models.TextField(null=True)
    social_rating = models.IntegerField(default=0)
    fishing_rating = models.IntegerField(default=0)
    views_blogs = models.IntegerField(default=0)
    view_reports = models.IntegerField(default=0)
    views_profile = models.IntegerField(default=0)
    count_blogs = models.IntegerField(default=0)
    count_comments = models.IntegerField(default=0)
    count_report = models.IntegerField(default=0)
    count_news = models.IntegerField(default=0)
    count_like = models.IntegerField(default=0)
    count_dislike = models.IntegerField(default=0)
    i_follow = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                              related_name='user_i_follow',null=True, blank=True)