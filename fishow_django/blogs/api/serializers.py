from rest_framework import serializers
from blogs.models import Blog, Comment, Prediction
from datetime import datetime,timezone
from django.utils.timesince import timesince


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    user_has_votedUp = serializers.SerializerMethodField()
    user_has_votedDown = serializers.SerializerMethodField()
    comments_slug = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ['blog', 'votersUp','votersDown', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.votersUp.count()

    def get_dislikes_count(self, instance):
        return instance.votersDown.count()

    def get_user_has_votedUp(self, instance):
        request = self.context.get("request")
        return instance.votersUp.filter(pk=request.user.pk).exists()

    def get_user_has_votedDown(self, instance):
        request = self.context.get("request")
        return instance.votersDown.filter(pk=request.user.pk).exists()

    def get_comments_slug(self, instance):
        return instance.blog.slug

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    user_has_votedUp = serializers.SerializerMethodField()
    user_has_votedDown = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    comments_count = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()
    time_from_creations = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        exclude = ['updated_at', 'votersUp','votersDown']

#     def get_created_at(self, instance):
#         return instance.created_at.strftime("%B %d, %Y")

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d.%m.%y %H:%M")

    def get_comments_count(self, instance):
        return instance.comments.count()

    def get_likes_count(self, instance):
        return instance.votersUp.count()

    def get_dislikes_count(self, instance):
        return instance.votersDown.count()

    def get_user_has_votedUp(self, instance):
        request = self.context.get("request")
        return instance.votersUp.filter(pk=request.user.pk).exists()

    def get_user_has_votedDown(self, instance):
        request = self.context.get("request")
        return instance.votersDown.filter(pk=request.user.pk).exists()

    def get_user_has_commented(self, instance):
        request = self.context.get('request')
        return instance.comments.filter(author=request.user).exists()

    def get_time_from_creations(self, object):
        created = object.created_at
        now = datetime.now(timezone.utc)
        time_spend = timesince(created, now)
        return time_spend

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
         model = Prediction
         field = '__all__'