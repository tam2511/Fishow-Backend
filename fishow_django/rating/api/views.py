from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from rating.api.serializers import Rating_regionSerializer,Rating_waterplaceSerializer
from report.api.permissions import IsAuthorOrReadOnly,DjangoObjectPermissionsOrAnonReadOnly
from report.models import Report, Comment_r, Fishing

from users.models import CustomUser

from django.contrib.auth.decorators import login_required


class Rating_waterplaceAPIView(APIView):
        queryset = Fishing.objects.all()
        serializer_class = Rating_waterplace


class Rating_regionAPIView(APIView):
        queryset = Fishing.objects.all()
        serializer_class = Rating_regionSerializer


