from django.db import models
from django.conf import settings


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    moderator_like = models.NullBooleanField(null=True, default=False)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="News")
    votersUp = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='votesUpNews')
    votersDown = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='votesDownNews')
    views = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                          related_name='viewsNews')


    def __str__(self):
        return self.slug

    class Meta:
        app_label = 'fishow_django'



class Comment_n(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='comments_n')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    votersUp = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='votesUp_n')
    votersDown = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='votesDown_n')

    def __str__(self):
        return self.author.username

    class Meta:
        app_label = 'fishow_django'
# # Create your models here.