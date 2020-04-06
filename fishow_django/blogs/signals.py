from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from blogs.models import Blog,Comment

from django.contrib.auth import get_user_model
from users.models import CustomUser

@receiver(pre_save, sender=Blog)
def add_slug_to_blog(sender, instance,*args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = slug + '-' + random_string

@receiver(pre_save, sender=Blog)
def count_plus_blog(sender, instance,*args,**kwargs):
    user=CustomUser.objects.get(username=instance.author)
    user.count_blogs=int(user.count_blogs)+1
    user.save()

@receiver(pre_delete, sender=Blog)
def dell_count_blog(sender, instance,*args,**kwargs):
    user=CustomUser.objects.get(username=instance.author)
    user.count_blogs=int(user.count_blogs)-1
    user.save()

@receiver(pre_save, sender=Comment)
def count_plus_blog(sender, instance,*args,**kwargs):
    user=CustomUser.objects.get(username=instance.author)
    user.count_comments=int(user.count_comments)+1
    user.save()

@receiver(pre_delete, sender=Comment)
def dell_count_blog(sender, instance,*args,**kwargs):
    user=CustomUser.objects.get(username=instance.author)
    user.count_comments=int(user.count_comments)-1
    user.save()