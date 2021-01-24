from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from space.api.serializers import Waterplace_natureSerializer, Waterplace_costSerializer, RegionSerializer
from space.api.permissions import DjangoObjectPermissionsOrAnonReadOnly
from space.models import Region, Waterplace_cost, Waterplace_nature

from users.models import CustomUser

from django.contrib.auth.decorators import login_required


# class Waterplace_costAPIView(APIView):
#         queryset = Waterplace_cost.objects.all()
#         serializer_class = Waterplace_costSerializer
#
# class Waterplace_natureAPIView(APIView):
#         queryset = Waterplace_nature.objects.all()
#         serializer_class = Waterplace_natureSerializer

class Waterplace_cost(viewsets.ModelViewSet):
        queryset = Waterplace_cost.objects.all()
        lookup_field = "slug"
        serializer_class = Waterplace_costSerializer
        permission_classes = [IsAuthenticated]

        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    if self.request.user.is_authenticated:
                        waterplace_cost=get_object_or_404(Waterplace_cost, slug = self.kwargs.get("slug"))
                    return obj

class Waterplace_nature(viewsets.ModelViewSet):
        queryset = Waterplace_nature.objects.all()
        lookup_field = "slug"
        serializer_class = Waterplace_natureSerializer
        permission_classes = [IsAuthenticated]

        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    if self.request.user.is_authenticated:
                        waterplace_nature=get_object_or_404(Waterplace_nature, slug = self.kwargs.get("slug"))
                    return obj



class Region(viewsets.ModelViewSet):
        queryset = Region.objects.all()
        lookup_field = "slug"
        serializer_class = RegionSerializer
        permission_classes = [IsAuthenticated]

        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    if self.request.user.is_authenticated:
                        region=get_object_or_404(Region, slug = self.kwargs.get("slug"))
                    return obj

