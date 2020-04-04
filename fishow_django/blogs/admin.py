from django.contrib import admin
from blogs.models import Blog, Comment, Prediction


admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Prediction)
# Register your models here.
