from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from rating.api.serializers import Rating_regionSerializer,Rating_waterplaceSerializer
from rating.api.permissions DjangoObjectPermissionsOrAnonReadOnly
from rating.models import Rating_region, Rating_waterplace

from users.models import CustomUser

from django.contrib.auth.decorators import login_required


class Rating_waterplaceAPIView(APIView):
        queryset = Rating_waterplace.objects.all()
        serializer_class = Rating_waterplace


class Rating_regionAPIView(APIView):
        queryset = Rating_region.objects.all()
        serializer_class = Rating_regionSerializer


