from rest_framework import serializers
from image.models import Image
from django.conf import settings



# class Statistics_main_pageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Statistics_main_page
#         fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
     image = serializers.ImageField(use_url=False)
     created_at = serializers.SerializerMethodField()
     image_url = serializers.SerializerMethodField()
     image_url_small = serializers.SerializerMethodField()
     image_url_large = serializers.SerializerMethodField()
     author = serializers.StringRelatedField(read_only=True)
     class Meta:
         model = Image
         ordering = ['-id']
         #fields = ['image']
         fields = '__all__'

     def get_image_url(self, instance):
             request = self.context.get('request')
             image = 'https://back.fishow.ru/media/'+str(instance.image)
             return request.build_absolute_uri(image)

     def get_image_url_small(self, instance):
             request = self.context.get('request')
             image = 'https://back.fishow.ru/media/thumbnails/'+str('.'.join(str(instance.image).split('.')[:-1]))+'_small.'+str(str(instance.image).split('.')[-1])
             return request.build_absolute_uri(image)

     def get_image_url_large(self, instance):
             request = self.context.get('request')
             image = 'https://back.fishow.ru/media/thumbnails/'+str('.'.join(str(instance.image).split('.')[:-1]))+'_large.'+str(str(instance.image).split('.')[-1])
             return request.build_absolute_uri(image)

     def get_created_at(self, instance):
         return instance.created_at.strftime("%d.%m.%y %H:%M")