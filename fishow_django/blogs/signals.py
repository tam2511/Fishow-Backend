from django.db.models.signals import pre_save,pre_delete
from django.core.signals import request_started,request_finished
from django.dispatch import receiver
#from django.utils.text import slugify
from pytils.translit import slugify
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
    if instance and not instance.id:
        user=CustomUser.objects.get(username=instance.author)
        user.count_comments=int(user.count_comments)+1
        user.save()

@receiver(pre_delete, sender=Comment)
def dell_count_blog(sender, instance,*args,**kwargs):
    user=CustomUser.objects.get(username=instance.author)
    user.count_comments=int(user.count_comments)-1
    user.save()

# @receiver(request_started)
# def priii(sender, *args,**kwargs):
# #@receiver(request_started,sender=Blog)
# #def priii(sender,instance *args,**kwargs):
#      info=kwargs['environ']
#      try:
#         if '/blog/' in info['HTTP_REFERER']:
#             if '/images/' not in info['HTTP_REFERER']:
#                 if 'GET' in info['REQUEST_METHOD']:
#                            print (info['HTTP_REFERER'])
#
# #                   for key, value in info.items():
# #                       if key in ["LC_CTYPE", "REQUEST_METHOD","HTTP_USER_AGENT","HTTP_REFERER","HTTP_ACCEPT_LANGUAGE"]:
# #                           print (key, value)
# #     except:
# #         pass