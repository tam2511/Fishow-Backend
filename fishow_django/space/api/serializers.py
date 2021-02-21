from rest_framework import serializers
from space.models import Region, Waterplace_cost, Waterplace_nature
from datetime import datetime,timezone
from django.utils.timesince import timesince
from blogs.api.serializers import BlogSerializerSlug

class Waterplace_natureSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    blogs = serializers.StringRelatedField(many=True)
    #reports = serializers.StringRelatedField(many=True)
    news = serializers.StringRelatedField(many=True)
    regions = serializers.SerializerMethodField()

    class Meta:
        model = Waterplace_nature
        fields = '__all__'

    def get_regions(self, instance):
        request = self.context.get("request")
        if Region.objects.filter(waterplace_nature=instance).exists():
            return Region.objects.filter(waterplace_nature=instance).values_list('slug',flat=True)
        else:
            return None

class Waterplace_costSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    blogs = serializers.StringRelatedField(many=True)
    #reports = serializers.StringRelatedField(many=True)
    news = serializers.StringRelatedField(many=True)
    regions = serializers.SerializerMethodField()

    class Meta:
        model = Waterplace_cost
        fields = '__all__'

    def get_regions(self, instance):
        request = self.context.get("request")
        if Region.objects.filter(waterplace_nature=instance).exists():
            return Region.objects.filter(waterplace_nature=instance).values_list('slug',flat=True)
        else:
            return None

class RegionSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    waterplace_cost = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Waterplace_cost.objects.all())
    waterplace_nature = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Waterplace_nature.objects.all())

    class Meta:
        model = Region
        fields = '__all__'
