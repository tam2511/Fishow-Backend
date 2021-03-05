from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from space.api.serializers import Waterplace_natureSerializer, Waterplace_costSerializer, RegionSerializer
from space.api.permissions import DjangoObjectPermissionsOrAnonReadOnly
from space.models import Region, Waterplace_cost, Waterplace_nature
from rest_framework import filters
from users.models import CustomUser
import json
from django.contrib.auth.decorators import login_required
from django.core import serializers

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
        permission_classes = [AllowAny]
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']

        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    return obj

class Waterplace_nature(viewsets.ModelViewSet):
        queryset = Waterplace_nature.objects.all()
        lookup_field = "slug"
        serializer_class = Waterplace_natureSerializer
        permission_classes = [AllowAny]
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']

        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    return obj



class RegionView(viewsets.ModelViewSet):
        queryset = Region.objects.all()
        lookup_field = "slug"
        serializer_class = RegionSerializer
        permission_classes = [AllowAny]
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']

        def get_object(self):
                    queryset = self.get_queryset()
                    obj=get_object_or_404(queryset,slug = self.kwargs.get("slug"))
                    print(self.request.user)
                    return obj


class Waterplace_cost_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stats=[]
        stats.append({'count_waterplace_cost':Waterplace_cost.objects.count()})
        return Response(stats)

class Waterplace_nature_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stats=[]
        stats.append({'count_waterplace_nature':Waterplace_nature.objects.count()})
        return Response(stats)

class Region_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stats=[]
        stats.append({'count_region':Region.objects.count()})
        return Response(stats)

class Region_list(APIView):
        permission_classes = [AllowAny]
        def get(self, request, format=None):
                regions = [{'region_name': region.name,'region_slug': region.slug} for region in Region.objects.all().order_by('name')]
                return Response(regions)

class SelectRegionAPIView(APIView):
        permission_classes = [AllowAny]
        def get(self, request, region):
            sities_list = get_object_or_404(Region, slug=region)
            #sities_list = Region.objects.get(slug=region)
#             print(sities_list.sities)
#             print(len("[\"\\u0410\\u0440\\u0445\\u0430\\u043d\\u0433\\u0435\\u043b\\u044c\\u0441\\u043a\", \"\\u041a\\u043e\\u0442\\u043b\\u0430\\u0441\", \"\\u0421\\u0435\\u0432\\u0435\\u0440\\u043e\\u0434\\u0432\\u0438\\u043d\\u0441\\u043a\"]"))
#             print(len(sities_list.sities))
#             print(type(sities_list.sities))
#             #print(serializers.serialize("json", sities_list))
#             print(json.loads("[\"\\u0411\\u0430\\u0440\\u043d\\u0430\\u0443\\u043b\", \"\\u0411\\u0438\\u0439\\u0441\\u043a\", \"\\u0420\\u0443\\u0431\\u0446\\u043e\\u0432\\u0441\\u043a\"]"))
#             print(json.loads(sities_list.sities))
#             #list=json.loads(sities_list.sities.encode('utf-8').decode('utf-8'))#.split(', '))
#             #print(list)
            return Response({'sities': sities_list.sities})