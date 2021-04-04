from rest_framework import serializers
from space.models import Region, Waterplace_cost, Waterplace_nature
from datetime import datetime,timezone
from django.utils.timesince import timesince
from blogs.api.serializers import BlogSerializerSlug

class RegionSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    waterplace_cost = serializers.SerializerMethodField()
    waterplace_nature = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = '__all__'

    def get_waterplace_nature(self, instance):
        request = self.context.get("request")
        if Waterplace_nature.objects.filter(regions=instance).exists():
            return Waterplace_nature.objects.filter(regions=instance).values_list('slug',flat=True)
        else:
            return None

    def get_waterplace_cost(self, instance):
        request = self.context.get("request")
        if Waterplace_cost.objects.filter(regions=instance).exists():
            return Waterplace_cost.objects.filter(regions=instance).values_list('slug',flat=True)
        else:
            return None

class Waterplace_natureSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    blogs = serializers.StringRelatedField(many=True)
    #reports = serializers.StringRelatedField(many=True)
    news = serializers.StringRelatedField(many=True)
    regions = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Region.objects.all())
    region_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Waterplace_nature
        fields = '__all__'

    def get_region_info(self, instance):
        list = []
        for i in instance.regions.all():
             list.append(ShortRegionSerializer(Region.objects.filter(slug=i),many=True).data[0])
        return list

class ShortWaterplace_costSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Waterplace_cost
        fields = ['slug','name']

class ShortWaterplace_natureSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Waterplace_nature
        fields = ['slug','name']

class ShortRegionSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Region
        fields = ['slug','name']

class Waterplace_costSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    blogs = serializers.StringRelatedField(many=True)
    #reports = serializers.StringRelatedField(many=True)
    news = serializers.StringRelatedField(many=True)
    regions = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Region.objects.all())
    region_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Waterplace_cost
        fields = '__all__'

    def get_region_info(self, instance):
        list = []
        for i in instance.regions.all():
             list.append(ShortRegionSerializer(Region.objects.filter(slug=i),many=True).data[0])
        return list

# class RegionListSerializer(serializers.ModelSerializer):
#
#     class Meta:
#             model = Region
#             fields = ['name','slug']