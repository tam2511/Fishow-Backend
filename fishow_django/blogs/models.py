from django.db import models
from django.conf import settings
from other_models.models import Tags


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.JSONField(default=dict,null=True)#models.TextField()
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags, related_name='b_tags', blank=True)#.JSONField(default={},null=True)#models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    moderator_like = models.BooleanField(null=True, default=False)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="blogs")
    saved = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='savedBlog')
    votersUp = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='votesUpBlog')
    votersDown = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='votesDownBlog')
    views = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='viewsBlog')

    def __str__(self):
        return self.slug


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

