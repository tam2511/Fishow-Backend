from django.db import models
from django.conf import settings

class Statistics_main_page(models.Model):
    prediction_quality_current = models.TextField(null=True)
    prediction_quality_old = models.TextField(null=True)
    count_reports = models.TextField(null=True)
    count_blogs = models.TextField(null=True)
    counts_users = models.TextField(null=True)


