from django.db.models.signals import pre_save,pre_delete
from django.core.signals import request_started,request_finished
from django.dispatch import receiver
from rest_framework.response import Response
#from django.utils.text import slugify
from pytils.translit import slugify
from core.utils import generate_random_string
from image.models import Image
import datetime
from django.contrib.auth import get_user_model
from users.models import CustomUser

# @receiver(pre_save, sender=Blog)
# def add_slug_to_blog(sender, instance,*args,**kwargs):
#     if instance and not instance.slug:
#         slug = slugify(instance.title)
#         random_string = generate_random_string()
#         instance.slug = slug + '-' + random_string
#
#         user=CustomUser.objects.get(username=instance.author)
#         user.count_blogs=int(user.count_blogs)+1
#         user.save()

# @receiver(pre_save, sender=Image)
# def change_info_image(sender, instance,*args,**kwargs):
#         if instance.type == 'blogs' or instance.type == 'news' or instance.type == 'reports' or instance.type == 'users' or instance.type == 'predictions' or instance.type == 'regions' or instance.type == 'waterplace_cost' or instance.type == 'waterplace_nature' or instance.type == 'comments':
#             now = datetime.datetime.now().strftime('%Y/%m/%d/%H/%M/%S/')
#             instance.image=instance.type + now + str(instance.image)
#         else:
#             now = datetime.datetime.now().strftime('%Y/%m/%d/%H/%M/%S/')
#             instance.image='trash/' + now + str(instance.image)

