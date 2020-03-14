from django.db import models
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    moderator_like = models.NullBooleanField(null=True, default=False)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="blogs")

    def __str__(self):
        return self.content


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    blog = models.ForeignKey(Blog,
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    votersUp = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='votesUp')
    votersDown = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='votesDown')

    def __str__(self):
        return self.author.username
# Create your models here.
