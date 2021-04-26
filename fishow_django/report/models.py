from django.db import models
from django.conf import settings
from space.models import Region, Waterplace_cost, Waterplace_nature


class Report(models.Model):
    title = models.CharField(max_length=100)
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)
    content = models.JSONField(default={},null=True)#models.TextField(null=True)
    fishing_report = models.JSONField(default={},null=True)#models.TextField(null=True)
    category = models.CharField(max_length=100)
    coordinates = models.TextField(null=True)
    tags = models.JSONField(default={},null=True)#models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    moderator_like = models.NullBooleanField(null=True, default=False)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="Reports")
    votersUp = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='votesUpReport')
    votersDown = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='votesDownReport')
    views = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='viewsReport')

    city = models.TextField(null=True)
    remark = models.TextField(null=True)
    region = models.ManyToManyField(Region, related_name="report_region", blank=True)
    waterplace_cost = models.ManyToManyField(Waterplace_cost, related_name="report_wcost", blank=True)
    waterplace_nature = models.ManyToManyField(Waterplace_nature, related_name="report_wnature", blank=True)

    def __str__(self):
        return self.slug


class Comment_r(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    report = models.ForeignKey(Report,
                               on_delete=models.CASCADE,
                               related_name='comments_r')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    votersUp = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='votesUp_r')
    votersDown = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='votesDown_r')

    def __str__(self):
        return self.author.username
