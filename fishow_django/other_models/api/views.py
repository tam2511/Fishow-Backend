from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from other_models.api.serializers import Statistics_main_pageSerializer
from other_models.api.permissions import DjangoObjectPermissionsOrAnonReadOnly
from other_models.models import Statistics_main_page

from django.contrib.auth.decorators import login_required
from django.core import serializers

class Statistics_main_pageView(viewsets.ModelViewSet):
        queryset = Statistics_main_page.objects.all()
        serializer_class = Statistics_main_pageSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]
