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
@receiver(pre_save, sender=Region)
def add_slug_to_news(sender, instance,*args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.name)
        random_string = generate_random_string()
        instance.slug = slug + '-' + random_string
