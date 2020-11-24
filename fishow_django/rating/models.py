from django.db import models
from django.conf import settings


class Report(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
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

    areal = models.TextField()
    city = models.TextField()

    def __str__(self):
        return self.content

class Fishing(models.Model):
    fish = models.TextField()
    estimation = models.TextField()
    type = models.TextField()

    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='fishing')

    def __str__(self):
        return self.content


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
# # Create your models here.