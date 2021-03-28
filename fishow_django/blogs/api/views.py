from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from django.shortcuts import get_list_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
import datetime
from django.db.models import Count

from blogs.api.serializers import BlogSerializer, CommentSerializer
from blogs.api.permissions import IsAuthorOrReadOnly,DjangoObjectPermissionsOrAnonReadOnly
from blogs.models import Blog, Comment
from rest_framework.parsers import MultiPartParser, FormParser
from users.models import CustomUser
from rest_framework import filters

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

        if user in [val for val in comment.votersUp.all()]:
            comment.votersUp.remove(user)
            comment.save()

            user=CustomUser.objects.get(username=comment.author)
            user.social_rating=int(user.social_rating)-1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_like=int(user.count_like)-1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(comment, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)


    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        if user not in [val for val in comment.votersUp.all()]:

            comment.votersUp.add(user)
            comment.save()

            user=CustomUser.objects.get(username=comment.author)
            user.social_rating=int(user.social_rating)+1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_like=int(user.count_like)+1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(comment, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)


class CommentDisLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        if user in [val for val in comment.votersDown.all()]:
            comment.votersDown.remove(user)
            comment.save()

            user=CustomUser.objects.get(username=comment.author)
            user.social_rating=int(user.social_rating)+1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_dislike=int(user.count_dislike)-1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(comment, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        if user not in [val for val in comment.votersDown.all()]:
            comment.votersDown.add(user)
            comment.save()

            user=CustomUser.objects.get(username=comment.author)
            user.social_rating=int(user.social_rating)-1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_dislike=int(user.count_dislike)+1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(comment, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
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
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
            if not self.request.user.is_anonymous:
                serializer.save(author=self.request.user)
    def get_object(self):
            queryset = self.get_queryset()
            obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
            self.check_object_permissions(self.request, obj)
            print(self.request.user)
            if self.request.user.is_authenticated:
                    blog=get_object_or_404(Blog, slug = self.kwargs.get("slug"))
                    user = self.request.user
                    print(user)
                    if user not in blog.views.all():
                        blog.views.add(user)
                        blog.save()
            return obj


class BlogLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, slug):
        """Remove request.user from the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, slug=slug)
        user = request.user

        if user in [val for val in blog.votersUp.all()]:
            blog.votersUp.remove(user)
            blog.save()

            user=CustomUser.objects.get(username=blog.author)
            user.social_rating=int(user.social_rating)-1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_like=int(user.count_like)-1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(blog, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, slug):
        """Add request.user to the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, slug=slug)
        user = request.user
#         send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, [request.user.email])
        if user not in [val for val in blog.votersUp.all()]:

            blog.votersUp.add(user)
            blog.save()

            user=CustomUser.objects.get(username=blog.author)
            user.social_rating=int(user.social_rating)+1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_like=int(user.count_like)+1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(blog, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

class BlogDisLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, slug):
        """Remove request.user from the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, slug=slug)
        user = request.user
        if user in [val for val in blog.votersDown.all()]:
            blog.votersDown.remove(user)
            blog.save()

            user=CustomUser.objects.get(username=blog.author)
            user.social_rating=int(user.social_rating)+1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_dislike=int(user.count_dislike)-1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(blog, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, slug):
        """Add request.user to the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, slug=slug)
        user = request.user
        if user not in [val for val in blog.votersDown.all()]:
            blog.votersDown.add(user)
            blog.save()

            user=CustomUser.objects.get(username=blog.author)
            user.social_rating=int(user.social_rating)-1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_dislike=int(user.count_dislike)+1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(blog, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

# class PredictionView(APIView):
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]

class BlogSaveAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, slug):
        """Remove request.user from the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, slug=slug)
        user = request.user

        if user in [val for val in blog.saved.all()]:
            blog.saved.remove(user)
            blog.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(blog, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, slug):
        """Add request.user to the voters queryset of an comment instance."""
        blog = get_object_or_404(Blog, slug=slug)
        user = request.user
#         send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, [request.user.email])
        if user not in [val for val in blog.saved.all()]:

            blog.saved.add(user)
            blog.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(blog, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)


class BlogUserSaved(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(saved=self.request.user).order_by("-created_at")

class BlogUserCreated(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user).order_by("-created_at")

class BlogUserSelectCreated(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs['username'])
        return Blog.objects.filter(author=user.id).order_by("-created_at")

class BlogUserLiked(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(votersUp=self.request.user).order_by("-created_at")

class BlogCommentUserLiked(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(votersUp=self.request.user).order_by("-created_at")

class BlogCommentUserCreated(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user).order_by("-created_at")

class Blogs_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stats=[]
        stats.append({'count_blogs':Blog.objects.count()})
        return Response(stats)

def modify_input_for_multiple_files(image):
    dict = {}
    dict['image'] = image
    return dict

class BlogFresh(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Blog.objects.all().order_by("-created_at")

class BlogBest(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Blog.objects.annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')


class BlogHot(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Blog.objects.filter(created_at__gte = datetime.datetime.now() - datetime.timedelta(days=1)).annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')