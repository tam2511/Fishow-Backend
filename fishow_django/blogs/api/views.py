from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from blogs.api.serializers import BlogSerializer, CommentSerializer
from blogs.api.permissions import IsAuthorOrReadOnly
from blogs.models import Blog, Comment


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    lookup_field = "slug"
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=kwarg_slug)
        serializer.save(author=request_user, blog=blog)


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comment.objects.filter(blog__slug=kwarg_slug).order_by("-created_at")