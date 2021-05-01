from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from other_models.api import views as qv

router = DefaultRouter()
router.register(r"statistics_main_page", qv.Statistics_main_pageView)
router.register(r"tags", qv.TagsView)
router.register(r"fishing_method", qv.Fishing_methodView)
router.register(r"nozzles", qv.NozzlesView)

urlpatterns = [
    path("", include(router.urls)),
]