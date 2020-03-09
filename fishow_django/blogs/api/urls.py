from django.urls import include, path
from rest_framework.routers import DefaultRouter
from blogs.api import views as qv

router = DefaultRouter()
router.register(r"blogs", qv.BlogViewSet)

urlpatterns = [
    path("", include(router.urls))
]