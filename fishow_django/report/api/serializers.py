from rest_framework import serializers
from report.models import Report, Comment_r
from datetime import datetime,timezone
from django.utils.timesince import timesince
from space.models import *


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
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

class ReportSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    waterplace_nature = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Waterplace_nature.objects.all())
    waterplace_cost = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Waterplace_cost.objects.all())
    region = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='slug',queryset=Region.objects.all())
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
