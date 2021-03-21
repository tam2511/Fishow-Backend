from rest_framework import serializers
from image.models import Image


# class Statistics_main_pageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Statistics_main_page
#         fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
     image = serializers.ImageField(use_url=False)
     image_url = serializers.SerializerMethodField()
     author = serializers.StringRelatedField(read_only=True)
     class Meta:
         model = Image
         ordering = ['-id']
         #fields = ['image']
         fields = '__all__'

     def get_image_url(self, instance):
             request = self.context.get('request')
             image = 'https://back.fishow.ru/'+str(instance.image)
             return request.build_absolute_uri(image)