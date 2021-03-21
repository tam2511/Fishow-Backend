from django.db import models
from django.conf import settings
import datetime
import os
from core.utils import generate_random_string

def change_info_image(instance,filename):
    if instance.type == 'blogs' or instance.type == 'news' or instance.type == 'reports' or instance.type == 'users' or instance.type == 'predictions' or instance.type == 'regions' or instance.type == 'waterplace_cost' or instance.type == 'waterplace_nature' or instance.type == 'comments':
        now = datetime.datetime.now().strftime('%Y/%m/%d/%H/%M/%S/')
        #instance.image=instance.type + now + str(instance.image)
        #return os.path.join(instance.type, now+filename)
        return os.path.join(instance.type, now+generate_random_string()+'.'+filename.split('.')[-1])
    else:
        now = datetime.datetime.now().strftime('%Y/%m/%d/%H/%M/%S/')
        #instance.image='trash/' + now + str(instance.image)
        print(filename)
        #return os.path.join('trash', now+filename)
        return os.path.join('trash', now+generate_random_string()+'.'+filename.split('.')[-1])

class Image(models.Model):
    image = models.FileField(null=True,upload_to=change_info_image)
    type = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="image_all")

