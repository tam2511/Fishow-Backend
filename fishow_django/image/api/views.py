from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from image.api.serializers import ImageSerializer
from image.models import Image

from django.contrib.auth.decorators import login_required
from django.core import serializers

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Image.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_anonymous:
            serializer.save(author=self.request.user)
        else:
            serializer_context = {'message':'error not auth'}
            return Response(serializer_context)

#     def pre_save(self, obj):
#             now = datetime.datetime.now().strftime('%Y/%m/%d/%H/%M/%S/')
#             print(now)
#             print(obj)
