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
import django_filters
import numpy as np
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

# class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
#     pass
#
# class DataFilter(django_filters.FilterSet):
#     keyword = CharInFilter(field_name='tags', lookup_expr='in')
#
#     class Meta:
#         model = Blog
#         fields = ['keyword']
#
# from django_filters import Filter
# from django_filters.fields import Lookup
#
# class ListFilter( Filter ):
#   def filter( self, qs, value ):
#     return super( ListFilter, self ).filter( qs, Lookup( value.split( u"," ), "in") )
#
# class ProductFilterSet(django_filters.FilterSet):
#     tags = ListFilter(name='tags__name')
#
#     class Meta:
#         model = Blog
#         fields = ['tags']

# class ChoiceFilter(django_filters.FilterSet):
#     tags__name = django_filters.MultipleChoiceFilter(
#         field_name='title',
#         lookup_expr='in',#'contains',
#         conjoined=True,  # uses AND instead of OR
#         #choices=['aa'],
#     )
#
#     class Meta:
#         model = Blog
#         fields = ['tags__name']


class MultiValueCharFilter(django_filters.BaseCSVFilter, django_filters.CharFilter):
    def filter(self, qs, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            qs = super(MultiValueCharFilter, self).filter(qs, value)

        return qs.annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')


class TagsFilter(django_filters.FilterSet):
    tags = MultiValueCharFilter(field_name='tags__name', lookup_expr='contains')

    class Meta:
        model = Blog
        fields = ['tags']


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by("-created_at").distinct()
    lookup_field = "slug"
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['tags__name']
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    #filterset_fields = ['tags__name']
    #search_fields = ['title']
    ordering_fields = ['created_at']
    #filter_fields = {'tags__name': ["in"]}
    #filter_fields = {'tags__name': ["in"]}
    filterset_class = TagsFilter

    def perform_create(self, serializer):
            if not self.request.user.is_anonymous:
                serializer.save(author=self.request.user)
    def get_object(self):
            queryset = self.get_queryset()
            obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
            self.check_object_permissions(self.request, obj)
            #print(self.request.user)
            if self.request.user.is_authenticated:
                    blog=get_object_or_404(Blog, slug = self.kwargs.get("slug"))
                    user = self.request.user
                    #print(user)
                    if user not in blog.views.all():
                        blog.views.add(user)
                        blog.save()
                        recom_content(user,blog)
#                         user.tags=blog.tags
#                         user.save()

            return obj

def recom_content(user,object):
    user_tags=user.tags
    object_tags=object.tags.all()
    for i in object_tags:
        i=str(i)
        try:
            user_tags[i]=int(user_tags[i])+1
        except:
            user_tags[i]=1
    curr_user=get_object_or_404(CustomUser, username = user)
    curr_user.tags=user_tags
    curr_user.save()



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
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        return Blog.objects.all().order_by("-created_at")

class BlogBest(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        return Blog.objects.annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')


class BlogHot(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        return Blog.objects.filter(created_at__gte = datetime.datetime.now() - datetime.timedelta(days=365)).annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')
        #return Blog.objects.annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum','-created_at')


class BlogNonviewed(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        arr=[]
        user = self.request.user
        for i in Blog.objects.all().order_by('-created_at'):
            if user not in [val for val in i.views.all()]:
                #print(i)
                arr.append(i)
        return arr#Blog.objects.filter(views = self.request.user).order_by('-created_at')

class BlogRecommend(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]

#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             arr=[]
#             blog_tags=[]
#             user = self.request.user
#             user_tags=user.tags
#             user_sort=dict(sorted(user_tags.items(), key=lambda item: item[1], reverse=True))
#             user_sort_tags=[i[0] for i in user_sort.items()]
#             print(user_sort)
#             print(user_sort_tags)
#             for i in Blog.objects.all().order_by('-created_at'):
#                 if user not in [val for val in i.views.all()]:
#                     arr.append(i)
#                 blog_tags.append([str(k) for k in i.tags.all()])
#             print(blog_tags)
#             print('-')
#             return ''
#         else:
#             return Blog.objects.filter(created_at__gte = datetime.datetime.now() - datetime.timedelta(days=1)).annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')

# def recom_content_out(user,object):
#     user_tags=user.tags
#     object_tags=object.tags.all()
#     for i in object_tags:
#         i=str(i)
#         try:
#             user_tags[i]=int(user_tags[i])+1
#         except:
#             user_tags[i]=1
#     curr_user=get_object_or_404(CustomUser, username = user)
#     curr_user.tags=user_tags
#     curr_user.save()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            arrr=[]
            user_sort_tags=[]
            user_sort_values=[]
            user = self.request.user
            #user_tags=user.tags
            #user_sort=dict(sorted(user_tags.items(), key=lambda item: item[1], reverse=True))
            user_sort = user.tags
            if len(user_sort) > 0:
                for i in user_sort.items():
                    user_sort_tags.append(i[0])#=[i[0] for i in user_sort.items()]
                    user_sort_values.append(i[1])#=np.array([user_sort[x] for x in user_sort_tags])
                user_sort_values=np.array(user_sort_values)
                veclen_user_sort_values= np.sqrt(user_sort_values.dot(user_sort_values))
                for i in Blog.objects.all().order_by('-created_at'):
                    if user not in [val for val in i.views.all()]:
                        blog_tags_curr = [str(k) for k in i.tags.all()]
                        bim=[user_sort[x] for x in set(user_sort_tags + blog_tags_curr) if x in user_sort_tags and x in blog_tags_curr]
                        bim = np.array(bim)
                        bim_lenght = np.sqrt(bim.dot(bim))
                        if bim_lenght/veclen_user_sort_values>0.75:
                            arrr.append(i)
                if len(arrr)>0:
                    return arrr
                else:
                    return Blog.objects.filter(created_at__gte = datetime.datetime.now() - datetime.timedelta(days=365)).annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')
            else:
                return Blog.objects.filter(created_at__gte = datetime.datetime.now() - datetime.timedelta(days=365)).annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')
        else:
            return Blog.objects.filter(created_at__gte = datetime.datetime.now() - datetime.timedelta(days=365)).annotate(fieldsum=Count('votersUp') - Count('votersDown')).order_by('-fieldsum')
