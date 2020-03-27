from rest_framework import serializers
from blogs.models import Blog, Comment


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

    class Meta:
        model = Blog
        exclude = ['updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

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
