from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from report.api.serializers import ReportSerializer, CommentSerializer
from report.api.permissions import IsAuthorOrReadOnly,DjangoObjectPermissionsOrAnonReadOnly
from report.models import Report, Comment_r
from rest_framework.parsers import MultiPartParser, FormParser
from users.models import CustomUser
from rest_framework import filters
from django.contrib.auth.decorators import login_required
import django_filters
from django.db.models import Count

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
        model = Report
        fields = ['tags']


class ReportView(viewsets.ModelViewSet):
        queryset = Report.objects.all().order_by("-created_at").distinct()
        lookup_field = "slug"
        serializer_class = ReportSerializer
        permission_classes = [IsAuthorOrReadOnly]
        #filter_backends = [filters.SearchFilter]
        filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
        ordering_fields = ['created_at']
        filterset_class = TagsFilter
        search_fields = ['title']

        def perform_create(self, serializer):
                    if not self.request.user.is_anonymous:
                        serializer.save(author=self.request.user)
        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    self.check_object_permissions(self.request, obj)
                    print(self.request.user)
                    if self.request.user.is_authenticated:
                            report=get_object_or_404(Report, slug = self.kwargs.get("slug"))
                            user = self.request.user
                            #print(user)
                            if user not in report.views.all():
                                report.views.add(user)
                                report.save()
                                #user.tags=report.tags
                                #user.save()
                                recom_content(user,report)
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

class ReportLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, slug):
        """Remove request.user from the voters queryset of an comment instance."""
        report = get_object_or_404(Report, slug=slug)
        user = request.user

        if user in [val for val in report.votersUp.all()]:
            report.votersUp.remove(user)
            report.save()

            user=CustomUser.objects.get(username=report.author)
            user.social_rating=int(user.social_rating)-1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_like=int(user.count_like)-1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(report, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, slug):
        """Add request.user to the voters queryset of an comment instance."""
        report = get_object_or_404(Report, slug=slug)
        user = request.user
#         send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, [request.user.email])
        if user not in [val for val in report.votersUp.all()]:

            report.votersUp.add(user)
            report.save()

            user=CustomUser.objects.get(username=report.author)
            user.social_rating=int(user.social_rating)+1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_like=int(user.count_like)+1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(report, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

class Report_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stats=[]
        stats.append({'count_report':Report.objects.count()})
        return Response(stats)

class ReportDisLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, slug):
        """Remove request.user from the voters queryset of an comment instance."""
        report = get_object_or_404(Report, slug=slug)
        user = request.user

        if user in [val for val in report.votersDown.all()]:
            report.votersDown.remove(user)
            report.save()

            user=CustomUser.objects.get(username=report.author)
            user.social_rating=int(user.social_rating)+1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_dislike=int(user.count_dislike)-1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(report, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, slug):
        """Add request.user to the voters queryset of an comment instance."""
        report = get_object_or_404(Report, slug=slug)
        user = request.user

        if user not in [val for val in report.votersDown.all()]:
            report.votersDown.add(user)
            report.save()

            user=CustomUser.objects.get(username=Report.author)
            user.social_rating=int(user.social_rating)-1
            user.save()

            user=CustomUser.objects.get(username=request.user)
            user.count_dislike=int(user.count_dislike)+1
            user.save()

            serializer_context = {"request": request}
            serializer = self.serializer_class(report, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment_r.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        report = get_object_or_404(Report, slug=kwarg_slug)
        serializer.save(author=request_user, report=report)

class CommentLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        comment = get_object_or_404(Comment_r, pk=pk)
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
        comment = get_object_or_404(Comment_r, pk=pk)
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
        comment = get_object_or_404(Comment_r, pk=pk)
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
        comment = get_object_or_404(Comment_r, pk=pk)
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

class ReportUserSelectCreated(generics.ListAPIView):
    serializer_class = ReportSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs['username'])
        return Report.objects.filter(author=user.id).order_by("-created_at")

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        kwarg_slug = self.kwargs.get("slug")
        return Comment_r.objects.filter(report__slug=kwarg_slug).order_by("-created_at")

class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an comment instance to it's author."""
    queryset = Comment_r.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]



#         def get_object(self):
#                     queryset = self.get_queryset()
#                     obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
#                     print(self.request.user)
#                     if self.request.user.is_authenticated:
#                             report=get_object_or_404(Report, pk=obj.id)
#                             user = self.request.user
#                             print(user)
#                             if user not in report.views.all():
#                                 report.views.add(user)
#                                 report.save()
#                     return obj
# class CommentCreateAPIView(generics.CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         request_user = self.request.user
#         kwarg_slug = self.kwargs.get("slug")
#         report = get_object_or_404(Report, slug=kwarg_slug)
#         serializer.save(author=request_user, report=report)
