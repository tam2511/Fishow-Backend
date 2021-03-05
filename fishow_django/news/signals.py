from django.db.models.signals import pre_save,pre_delete
from django.core.signals import request_started,request_finished
from django.dispatch import receiver
#from django.utils.text import slugify
from pytils.translit import slugify
from core.utils import generate_random_string
from news.models import News,Comment_n

from django.contrib.auth import get_user_model
from users.models import CustomUser

@receiver(pre_save, sender=News)
def add_slug_to_news(sender, instance,*args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = slug + '-' + random_string

        user=CustomUser.objects.get(username=instance.author)
        user.count_news=int(user.count_news)+1
        user.save()

@receiver(pre_delete, sender=News)
def dell_count_news(sender, instance,*args,**kwargs):
    user=CustomUser.objects.get(username=instance.author)
    user.count_news=int(user.count_news)-1
    user.save()

@receiver(pre_save, sender=Comment_n)
def count_plus_news(sender, instance,*args,**kwargs):
    if instance and not instance.id:
        user=CustomUser.objects.get(username=instance.author)
        user.count_comments=int(user.count_comments)+1
        user.save()

@receiver(pre_delete, sender=Comment_n)
def dell_count_news(sender, instance,*args,**kwargs):
    user=CustomUser.objects.get(username=instance.author)
    user.count_comments=int(user.count_comments)-1
    user.save()
