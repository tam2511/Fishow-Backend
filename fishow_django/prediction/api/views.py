from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from prediction.api.serializers import PredictionSerializer,PredictiontenSerializer
from blogs.api.permissions import DjangoObjectPermissionsOrAnonReadOnly
from prediction.models import Prediction,Predictionten



class PredictionView(viewsets.ModelViewSet):
        queryset = Prediction.objects.all().order_by('id')

        serializer_class = PredictionSerializer
        permission_classes = [DjangoObjectPermissionsOrAnonReadOnly]
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['areal','date','city','fish']

        def perform_create(self, serializer):
            serializer.save()

class PredictiontenView(viewsets.ModelViewSet):
        queryset = Predictionten.objects.all().order_by('id')

        serializer_class = PredictiontenSerializer
        permission_classes = [DjangoObjectPermissionsOrAnonReadOnly]
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['areal','date','city','fish']

        def perform_create(self, serializer):
            serializer.save()

class Prediction_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stats=[]
        stats.append({'count_prediction':Prediction.objects.count()})
        return Response(stats)