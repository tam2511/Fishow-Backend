from rest_framework import serializers
from blogs.models import Blog, Comment
from other_models.models import Tags
from datetime import datetime,timezone
from django.utils.timesince import timesince
from users.api.serializers import ShortUserDisplaySerializer


class CommentSerializer(serializers.ModelSerializer):
    author = ShortUserDisplaySerializer(read_only=True)
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
        return instance.blog.slug

class BlogSerializer(serializers.ModelSerializer):
    author = ShortUserDisplaySerializer(read_only=True)
    tags = serializers.SlugRelatedField(many=True,allow_null=True,slug_field='name',queryset=Tags.objects.all())
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    user_has_votedUp = serializers.SerializerMethodField()
    user_has_votedDown = serializers.SerializerMethodField()
    user_saved = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    comments_count = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()
    time_from_creations = serializers.SerializerMethodField()
    user_views = serializers.SerializerMethodField()
    is_author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        exclude = ['updated_at', 'votersUp','votersDown','saved','views']

    def get_is_author(self, instance):
        request = self.context.get("request")
        if request.user == instance.author:
            return True
        else:
            return False

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

    def get_user_saved(self, instance):
        request = self.context.get("request")
        if not request.user.is_anonymous:
            return instance.saved.filter(pk=request.user.pk).exists()
        else:
            return False

    def get_user_has_commented(self, instance):
        request = self.context.get('request')
        if not request.user.is_anonymous:
            return instance.comments.filter(author=request.user).exists()
        else:
            return False

    def get_time_from_creations(self, object):
        created = object.created_at
        now = datetime.now(timezone.utc)
        time_spend = timesince(created, now)
        return time_spend

    def get_user_views(self, instance):
        return instance.views.count()

class BlogSerializerSlug(serializers.ModelSerializer):
    slug = serializers.SlugField()

    class Meta:
        model = Blog
        fields = ['slug']
