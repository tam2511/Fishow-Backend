from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from other_models.api import views as qv

router = DefaultRouter()
router.register(r"statistics_main_page", qv.Statistics_main_pageView)

urlpatterns = [
    path("", include(router.urls)),
]