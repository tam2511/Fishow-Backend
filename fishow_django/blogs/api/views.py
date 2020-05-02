from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from blogs.api.serializers import BlogSerializer, CommentSerializer
from blogs.api.permissions import IsAuthorOrReadOnly,DjangoObjectPermissionsOrAnonReadOnly
from blogs.models import Blog, Comment

from users.models import CustomUser

from django.contrib.auth.decorators import login_required

# from django.conf import settings
# from django.core.mail import send_mail


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=kwarg_slug)
        serializer.save(author=request_user, blog=blog)

class CommentLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.votersUp.remove(user)
        comment.save()

        user=CustomUser.objects.get(username=request.user)
        user.rating=int(user.rating)-1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.votersUp.add(user)
        comment.save()

        user=CustomUser.objects.get(username=request.user)
        user.rating=int(user.rating)+1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentDisLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.votersDown.remove(user)
        comment.save()

        user=CustomUser.objects.get(username=request.user)
        user.rating=int(user.rating)+1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.votersDown.add(user)
        comment.save()

        user=CustomUser.objects.get(username=request.user)
        user.rating=int(user.rating)-1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comment.objects.filter(blog__slug=kwarg_slug).order_by("-created_at")

class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an comment instance to it's author."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly,DjangoObjectPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
            if not self.request.user.is_anonymous:
                serializer.save(author=self.request.user)


class BlogLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, pk=pk)
        user = request.user

        blog.votersUp.remove(user)
        blog.save()

        user=CustomUser.objects.get(username=request.user)
        user.rating=int(user.rating)-1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(blog, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, pk=pk)
        user = request.user
#         send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, [request.user.email])
        blog.votersUp.add(user)
        blog.save()

        user=CustomUser.objects.get(username=request.user)
        user.rating=int(user.rating)+1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(blog, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogDisLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, pk=pk)
        user = request.user

        blog.votersDown.remove(user)
        blog.save()

        user=CustomUser.objects.get(username=request.user)
        user.rating=int(user.rating)+1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(blog, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, pk=pk)
        user = request.user

        blog.votersDown.add(user)
        blog.save()

        user=CustomUser.objects.get(username=request.user)
        user.rating=int(user.rating)-1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(blog, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

# class PredictionView(APIView):
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]

