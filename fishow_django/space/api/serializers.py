from rest_framework import serializers
from space.models import Region, Waterplace_cost, Waterplace_nature
from datetime import datetime,timezone
from django.utils.timesince import timesince
from blogs.api.serializers import BlogSerializerSlug

class Waterplace_natureSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(many=True)
    blogs = serializers.StringRelatedField(many=True)
    reports = serializers.StringRelatedField(many=True)
    news = serializers.StringRelatedField(many=True)
    class Meta:
        model = Waterplace_nature
        fields = '__all__'

class Waterplace_costSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
#     blogs = BlogSerializerSlug(many=True)
#     reports = serializers.StringRelatedField(many=True)
#     news = serializers.StringRelatedField(many=True)
    class Meta:
        model = Waterplace_cost
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    #waterplace_cost = serializers.StringRelatedField(many=True)
    #waterplace_nature = serializers.StringRelatedField(many=True)
    class Meta:
        model = Region
        fields = '__all__'