from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    country = models.TextField(null=True)
    city = models.TextField(null=True)
    avatar = models.TextField(null=True)
    about = models.TextField(null=True)
    tags = models.JSONField(default=dict,null=True)#models.TextField(null=True)
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
                                              related_name='user_i_follow', blank=True)
# class LogUserViews(models.Model):
#     viewed_at = models.DateTimeField(auto_now_add=True)
#     type = models.TextField()
#     slug = models.TextField()
#     tags = models.JSONField(default={},null=True)