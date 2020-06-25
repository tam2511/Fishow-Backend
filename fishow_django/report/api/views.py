from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from report.api.serializers import ReportSerializer#, CommentSerializer
from blogs.api.permissions import IsAuthorOrReadOnly,DjangoObjectPermissionsOrAnonReadOnly
from report.models import Report#, Comment, Fishing

from users.models import CustomUser

from django.contrib.auth.decorators import login_required


class ReportView(viewsets.ModelViewSet):
        queryset = Report.objects.all()
        serializer_class = ReportSerializer
        permission_classes = [DjangoObjectPermissionsOrAnonReadOnly]
        #filter_backends = [DjangoFilterBackend]
        filterset_fields = ['areal','time','date','city','fish']

        def perform_create(self, serializer):
                    if not self.request.user.is_anonymous:
                        serializer.save(author=self.request.user)
        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    if self.request.user.is_authenticated:
                            blog=get_object_or_404(Report, pk=obj.id)
                            user = self.request.user
                            print(user)
                            if user not in report.views.all():
                                report.views.add(user)
                                report.save()
                    return obj

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
