from django.urls import include, path
from rest_framework.routers import DefaultRouter
from prediction.api import views as qv
from prediction.models import Prediction

router = DefaultRouter()
router.register(r"prediction", qv.PredictionView)
router.register(r"predictionten", qv.PredictiontenView)

urlpatterns = [
    path("", include(router.urls)),
    path("count/prediction/", qv.Prediction_count.as_view(), name='prediction_count'),

]