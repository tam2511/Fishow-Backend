from django.contrib import admin
from blogs.models import Blog, Comment, Image


admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Image)
# Register your models here.
