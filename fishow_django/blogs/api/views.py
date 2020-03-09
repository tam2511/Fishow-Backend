from rest_framework import  viewsets

from rest_framework.permissions import IsAuthenticated
from blogs.api.serializers import BlogSerializer
from blogs.api.permissions import IsAuthorOrReadOnly
from blogs.models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    lookup_field = "slug"
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)