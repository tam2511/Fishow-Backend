from rest_framework import serializers
from other_models.models import Statistics_main_page, Tags, Fishing_method, Nozzles
from blogs.models import Blog


class Statistics_main_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics_main_page
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
     count=serializers.SerializerMethodField(read_only=True)

     class Meta:
         ordering = ['-count']
         model = Tags
         fields = ['name','count']

     def get_count(self,instance):
             return instance.b_tags.count()+instance.n_tags.count()+instance.r_tags.count()

class Fishing_methodSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-name']
        model = Fishing_method
        fields = ['name']

class NozzlesSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-name']
        model = Nozzles
        fields = ['name']
