from django.db import models
from django.conf import settings

class Statistics_main_page(models.Model):
    prediction_quality_current = models.TextField(null=True)
    prediction_quality_old = models.TextField(null=True)
    count_reports = models.TextField(null=True)
    count_blogs = models.TextField(null=True)
    counts_users = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

class Tags(models.Model):
    name = models.CharField(max_length=100)
    #count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="author_tags")

    def __str__(self):
        return self.name

class Fishing_method(models.Model):
    name = models.CharField(max_length=100)
    #count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="author_fm")

    def __str__(self):
        return self.name

class Nozzles(models.Model):
    name = models.CharField(max_length=100)
    #count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="author_nozzles")

    def __str__(self):
        return self.name




