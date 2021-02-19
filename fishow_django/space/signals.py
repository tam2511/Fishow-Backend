from django.db.models.signals import pre_save
from django.core.signals import request_started,request_finished
from django.dispatch import receiver
#from django.utils.text import slugify
from pytils.translit import slugify
from core.utils import generate_random_string
from space.models import Region, Waterplace_cost, Waterplace_nature

from django.contrib.auth import get_user_model
from users.models import CustomUser

@receiver(pre_save, sender=Waterplace_nature)
@receiver(pre_save, sender=Waterplace_cost)
def add_slug_to_waterplace(sender, instance,*args,**kwargs):
    if instance and not instance.slug:
        slug1 = slugify(instance.type)
        slug2 = slugify(instance.name)
        random_string = generate_random_string()
        instance.slug = slug1 + slug2 + '-' + random_string

@receiver(pre_save, sender=Region)
def add_slug_to_region(sender, instance,*args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.name)
        random_string = generate_random_string()
        instance.slug = slug + '-' + random_string