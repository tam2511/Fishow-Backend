from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from image.api import views as qv

router = DefaultRouter()
router.register(r"images", qv.ImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]