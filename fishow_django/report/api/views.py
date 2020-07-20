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
        queryset = Report.objects.all().order_by("-created_at")
        lookup_field = "slug"
        serializer_class = ReportSerializer
        permission_classes = [IsAuthorOrReadOnly]

        def perform_create(self, serializer):
                    if not self.request.user.is_anonymous:
                        serializer.save(author=self.request.user)
        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    if self.request.user.is_authenticated:
                            report=get_object_or_404(Report, pk=obj.id)
                            user = self.request.user
                            print(user)
                            if user not in report.views.all():
                                report.views.add(user)
                                report.save()
                    return obj

class ReportLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        report = get_object_or_404(Report, pk=pk)
        user = request.user

        report.votersUp.remove(user)
        report.save()

        user=CustomUser.objects.get(username=request.user)
        user.fishing_rating=int(user.fishing_rating)-1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(report, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        report = get_object_or_404(Report, pk=pk)
        user = request.user
#         send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, [request.user.email])
        report.votersUp.add(user)
        report.save()

        user=CustomUser.objects.get(username=request.user)
        user.fishing_rating=int(user.fishing_rating)+1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(report, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ReportDisLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comment instance."""
        report = get_object_or_404(Report, pk=pk)
        user = request.user

        report.votersDown.remove(user)
        report.save()

        user=CustomUser.objects.get(username=request.user)
        user.fishing_rating=int(user.fishing_rating)+1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(report, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comment instance."""
        report = get_object_or_404(Report, pk=pk)
        user = request.user

        report.votersDown.add(user)
        report.save()

        user=CustomUser.objects.get(username=request.user)
        user.fishing_rating=int(user.fishing_rating)-1
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(report, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


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
