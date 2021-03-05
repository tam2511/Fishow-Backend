from django.db import models
from django.conf import settings
from blogs.models import Blog
from news.models import News
#from report.models import Report

class Region(models.Model):
    name = models.CharField(max_length=100)
    stat = models.TextField(null=True)
    tourbases = models.TextField(null=True)  # models.ForeignKey(Tourbases)
    descriptions = models.TextField(null=True)
    representatives = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='representatives_people',
                                             blank=True)
    sities = models.TextField(null=True)
    #waterplace_cost = models.ManyToManyField(Waterplace_cost, related_name="region_w_cost", blank=True)
    #waterplace_nature = models.ManyToManyField(Waterplace_nature, related_name="region_w_nature", blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.slug

class Waterplace_nature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    type = models.TextField(null=True)
    fish = models.TextField(null=True)
    news = models.ManyToManyField(News, related_name='wn_news', blank=True)
    blogs = models.ManyToManyField(Blog, related_name='wn_blogs', blank=True)
    #reports = models.ManyToManyField(Report, related_name='wn_reports', blank=True)
    moderators = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="wn_moderators", null=True, blank=True)
    # town = models.ForeignKey(Rating_Region,related_name='town_region')
    moderators_share = models.TextField(null=True)
    city_list = models.TextField(null=True)
    stat = models.TextField(null=True)
    fish_rating = models.TextField(null=True)
    regions = models.ManyToManyField(Region, related_name="region_w_nature", blank=True)
    tour_base = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True)
    rating = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.slug


class Waterplace_cost(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    type = models.TextField(null=True)
    fish = models.TextField(null=True)
    news = models.ManyToManyField(News, related_name='wc_news', blank=True)
    blogs = models.ManyToManyField(Blog, related_name='wc_blogs', blank=True)
    #reports = models.ManyToManyField(Report, related_name='wc_reports', blank=True)
    moderators = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="wc_moderators", null=True, blank=True)
    # town = models.ForeignKey(Rating_Region,related_name='town_region')
    moderators_share = models.TextField(null=True)
    city_list = models.TextField(null=True)
    stat = models.TextField(null=True)
    fish_rating = models.TextField(null=True)
    regions = models.ManyToManyField(Region, related_name="region_w_cost", blank=True)
    tour_base = models.TextField(null=True)
    price = models.TextField(null=True)
    address = models.TextField(null=True)
    coordinates = models.TextField(null=True)
    is_paid = models.NullBooleanField(null=True, default=False)
    last_fishing = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True)
    rating = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.slug
