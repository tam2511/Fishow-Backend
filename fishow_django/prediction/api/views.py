from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from prediction.api.serializers import PredictionSerializer
# from prediction.api.permissions import IsAuthorOrReadOnly
from prediction.models import Prediction



class PredictionView(viewsets.ModelViewSet):
        queryset = Prediction.objects.all()

        serializer_class = PredictionSerializer
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            serializer.save()
