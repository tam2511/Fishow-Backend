from rest_framework import serializers
from blogs.models import Blog, Comments


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        exclude = ['blog', 'voters', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d %Y")

    def get_created_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    comments_count = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        exclude = ['updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d %Y")

    def get_comments_count(self, instance):
        return instance.comments.count()

    def get_user_has_commented(self, instance):
        request = self.context.get('request')
        return instance.comments.filter(author=request.user).exists()
