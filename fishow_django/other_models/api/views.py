from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from other_models.api.serializers import Statistics_main_pageSerializer, TagsSerializer, Fishing_methodSerializer, NozzlesSerializer
from other_models.api.permissions import DjangoObjectPermissionsOrAnonReadOnly
from other_models.models import Statistics_main_page, Tags, Fishing_method, Nozzles

from django.contrib.auth.decorators import login_required
from django.core import serializers
from rest_framework import filters

class Statistics_main_pageView(viewsets.ModelViewSet):
        queryset = Statistics_main_page.objects.all()
        serializer_class = Statistics_main_pageSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]

class TagsView(viewsets.ModelViewSet):
        queryset = Tags.objects.all()
        serializer_class = TagsSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']

#         def perform_create(self, serializer):
#                     if not self.request.user.is_anonymous:
#                         serializer.save(author=self.request.user)
#
#         def create(self, request, *args, **kwargs):
#                  data=request.data
#                  many = True if isinstance(data, list) else False
#
#                  if many==True:
#                     if len(data)>20:
#                         serializer_context = {'message':'error max tags'}
#                         return Response(serializer_context)
#                     data=[]
#                     for item in request.data:
#                         if self.get_serializer(data=item, many=False).is_valid()==True:
#                             data.append(item)
#                     if len(data)==0:
#                         serializer_context = {'message':'all tags exist'}
#                         return Response(serializer_context)
#                  serializer = self.get_serializer(data=data, many=many)
#                  serializer.is_valid(raise_exception=True)
#                  self.perform_create(serializer)
#                  headers = self.get_success_headers(serializer.data)
#                  return Response({'message':'ok'}, status=status.HTTP_201_CREATED, headers=headers)

class Fishing_methodView(viewsets.ModelViewSet):
        queryset = Fishing_method.objects.all()
        serializer_class = Fishing_methodSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']

        def perform_create(self, serializer):
                    if not self.request.user.is_anonymous:
                        serializer.save(author=self.request.user)

class NozzlesView(viewsets.ModelViewSet):
        queryset = Nozzles.objects.all()
        serializer_class = NozzlesSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']

        def perform_create(self, serializer):
                    if not self.request.user.is_anonymous:
                        serializer.save(author=self.request.user)