from django.db import models
from django.conf import settings
from blogs.models import Blog
from news.models import News
from report.models import Report


class Waterplace_nature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fish = models.TextField()
    news = models.ManyToManyField(News,related_name='wn_news',blank=True)
    blogs = models.ManyToManyField(Blog,related_name='wn_blogs',blank=True)
    reports = models.ManyToManyField(Report,related_name='wn_reports',blank=True)
    moderators = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="wn_moderators")
    #town = models.ForeignKey(Rating_Region,related_name='town_region')
    moderators_share = models.TextField()
    city_list = models.TextField()
    fish_rating = models.TextField()
    region_list = models.TextField() #models
    tour_base = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.slug

class Waterplace_cost(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fish = models.TextField()
    news = models.ManyToManyField(News,related_name='wc_news',blank=True)
    blogs = models.ManyToManyField(Blog,related_name='wc_blogs',blank=True)
    reports = models.ManyToManyField(Report,related_name='wc_reports',blank=True)
    moderators = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="wc_moderators")
    #town = models.ForeignKey(Rating_Region,related_name='town_region')
    moderators_share = models.TextField()
    city_list = models.TextField()
    fish_rating = models.TextField()
    region_list = models.TextField() #models
    tour_base = models.TextField()
    price = models.TextField()
    address = models.TextField()
    coordinates = models.TextField()
    is_paid = models.NullBooleanField(null=True, default=False)
    last_fishing = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.slug

class Region(models.Model):
    name = models.CharField(max_length=100)
    statistic_fishing = models.CharField(max_length=100)
    tourbases = models.TextField()#models.ForeignKey(Tourbases)
    descriptions = models.TextField()
    representatives = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='representatives_people',blank=True)
    sities = models.TextField()
    waterplace_cost = models.ManyToManyField(Waterplace_nature,related_name="cost",blank=True)
    waterplace_nature = models.ManyToManyField(Waterplace_nature,related_name="nature",blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.slug


