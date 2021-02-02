from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from news.api.serializers import NewsSerializer, CommentSerializer
from news.api.permissions import IsAuthorOrReadOnly,DjangoObjectPermissionsOrAnonReadOnly
from news.models import News, Comment_n
from rest_framework.parsers import MultiPartParser, FormParser
from users.models import CustomUser
from rest_framework import filters
from django.contrib.auth.decorators import login_required


class NewsView(viewsets.ModelViewSet):
        queryset = News.objects.all().order_by("-created_at")
        lookup_field = "slug"
        serializer_class = NewsSerializer
        permission_classes = [IsAuthorOrReadOnly]
        filter_backends = [filters.SearchFilter]
        search_fields = ['title', 'content']

        def perform_create(self, serializer):
                    if not self.request.user.is_anonymous:
                        serializer.save(author=self.request.user)
        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    if self.request.user.is_authenticated:
                            news=get_object_or_404(News, slug = self.kwargs.get("slug"))
                            user = self.request.user
                            print(user)
                            if user not in news.views.all():
                                news.views.add(user)
                                news.save()
                    return obj

class NewsLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        news = get_object_or_404(News, slug=slug)
        user = request.user

        if user in [val for val in news.votersUp.all()]:
            news.votersUp.remove(user)
            news.save()

            user=CustomUser.objects.get(username=news.author)
            user.social_rating=int(user.social_rating)-1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_like=int(user.count_like)-1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(news, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        news = get_object_or_404(News, slug=slug)
        user = request.user
#         send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, [request.user.email])
        if user not in [val for val in news.votersUp.all()]:

            news.votersUp.add(user)
            news.save()

            user=CustomUser.objects.get(username=news.author)
            user.social_rating=int(user.social_rating)+1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_like=int(user.count_like)+1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(news, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)


class NewsDisLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        news = get_object_or_404(News, slug=slug)
        user = request.user

        if user in [val for val in news.votersDown.all()]:
            news.votersDown.remove(user)
            news.save()

            user=CustomUser.objects.get(username=news.author)
            user.social_rating=int(user.social_rating)+1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_dislike=int(user.count_dislike)-1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(news, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        news = get_object_or_404(News, slug=slug)
        user = request.user

        if user not in [val for val in news.votersDown.all()]:
            news.votersDown.add(user)
            news.save()

            user=CustomUser.objects.get(username=News.author)
            user.social_rating=int(user.social_rating)-1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_dislike=int(user.count_dislike)+1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(news, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment_n.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        news = get_object_or_404(News, slug=kwarg_slug)
        serializer.save(author=request_user, news=news)

class CommentLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment_n, pk=pk)
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
        comment = get_object_or_404(Comment_n, pk=pk)
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
        comment = get_object_or_404(Comment_n, pk=pk)
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
        comment = get_object_or_404(Comment_n, pk=pk)
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
        return Comment_n.objects.filter(news__slug=kwarg_slug).order_by("-created_at")

class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an comment instance to it's author."""
    queryset = Comment_n.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class News_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stats=[]
        stats.append({'count_news':News.objects.count()})
        return Response(stats)


#         def get_object(self):
#                     queryset = self.get_queryset()
#                     obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
#                     print(self.request.user)
#                     if self.request.user.is_authenticated:
#                             news=get_object_or_404(News, pk=obj.id)
#                             user = self.request.user
#                             print(user)
#                             if user not in news.views.all():
#                                 news.views.add(user)
#                                 news.save()
#                     return obj
# class CommentCreateAPIView(generics.CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         request_user = self.request.user
#         kwarg_slug = self.kwargs.get("slug")
#         news = get_object_or_404(News, slug=kwarg_slug)
#         serializer.save(author=request_user, news=news)
