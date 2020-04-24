from django.urls import include, path
from rest_framework.routers import DefaultRouter
from prediction.api import views as qv

router = DefaultRouter()
router.register(r"prediction", qv.PredictionView)
router.register(r"predictionten", qv.PredictiontenView)

urlpatterns = [
    path("", include(router.urls)),
]