from rest_framework import serializers
from report.models import Report, Comment_r
from datetime import datetime,timezone
from django.utils.timesince import timesince
from space.models import *
from users.api.serializers import ShortUserDisplaySerializer
from space.api.serializers import ShortWaterplace_costSerializer,ShortWaterplace_natureSerializer,ShortRegionSerializer
from other_models.models import Tags

class CommentSerializer(serializers.ModelSerializer):
    author = ShortUserDisplaySerializer(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    user_has_votedUp = serializers.SerializerMethodField()
    user_has_votedDown = serializers.SerializerMethodField()
    comments_slug = serializers.SerializerMethodField()

    class Meta:
        model = Comment_r
        exclude = ['report', 'votersUp','votersDown', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.votersUp.count()

    def get_dislikes_count(self, instance):
        return instance.votersDown.count()

    def get_user_has_votedUp(self, instance):
        request = self.context.get("request")
        if not request.user.is_anonymous:
            return instance.votersUp.filter(pk=request.user.pk).exists()
        else:
            return False

    def get_user_has_votedDown(self, instance):
        request = self.context.get("request")
        if not request.user.is_anonymous:
            return instance.votersDown.filter(pk=request.user.pk).exists()
        else:
            return False

    def get_comments_slug(self, instance):
        return instance.report.slug

class MyListingField(serializers.RelatedField):

    def to_representation(self, value):
        return 'name: %s , slug: %s' % (value.name, value.name)

class ReportSerializer(serializers.ModelSerializer):
    author = ShortUserDisplaySerializer(read_only=True)
    coordinates = serializers.CharField(max_length=100, allow_blank=True)
    created_at = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='name',queryset=Tags.objects.all())
    waterplace_nature = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Waterplace_nature.objects.all())
    waterplace_nature_info = serializers.SerializerMethodField(read_only=True)
    waterplace_cost = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Waterplace_cost.objects.all())
    waterplace_cost_info = serializers.SerializerMethodField(read_only=True)
    region = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Region.objects.all())
    region_info = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    user_has_votedUp = serializers.SerializerMethodField()
    user_has_votedDown = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    comments_count = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()
    time_from_creations = serializers.SerializerMethodField()
    user_views = serializers.SerializerMethodField()

    class Meta:
        model = Report
        exclude = ['updated_at', 'votersUp','votersDown','views']

#     def create(self, validated_data):
#             wcs_data = validated_data.pop('waterplace_cost')
#             report = Report.objects.create(**validated_data)
#             for wc in wcs_data:
#                 Waterplace_cost.objects.create(report=report, **track_data)
#             return report

    def get_waterplace_cost_info(self, instance):
        list = []
        for i in instance.waterplace_cost.all():
             list.append(ShortWaterplace_costSerializer(Waterplace_cost.objects.filter(slug=i),many=True).data[0])
        return list

    def get_waterplace_nature_info(self, instance):
        list = []
        for i in instance.waterplace_nature.all():
             list.append(ShortWaterplace_natureSerializer(Waterplace_nature.objects.filter(slug=i),many=True).data[0])
        return list

    def get_region_info(self, instance):
        list = []
        for i in instance.region.all():
             list.append(ShortRegionSerializer(Region.objects.filter(slug=i),many=True).data[0])
        return list

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d.%m.%y %H:%M")

    def get_comments_count(self, instance):
            return instance.comments_r.count()

    def get_likes_count(self, instance):
        return instance.votersUp.count()

    def get_dislikes_count(self, instance):
        return instance.votersDown.count()

    def get_user_has_votedUp(self, instance):
        request = self.context.get("request")
        if not request.user.is_anonymous:
            return instance.votersUp.filter(pk=request.user.pk).exists()
        else:
            return False

    def get_user_has_votedDown(self, instance):
        request = self.context.get("request")
        if not request.user.is_anonymous:
            return instance.votersDown.filter(pk=request.user.pk).exists()
        else:
            return False

    def get_user_has_commented(self, instance):
        request = self.context.get('request')
        if not request.user.is_anonymous:
            return None #instance.comments.filter(author=request.user).exists()
        else:
            return False

    def get_time_from_creations(self, object):
        created = object.created_at
        now = datetime.now(timezone.utc)
        time_spend = timesince(created, now)
        return time_spend

    def get_user_views(self, instance):
        return instance.views.count()
