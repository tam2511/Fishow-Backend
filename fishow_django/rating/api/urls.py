from django.urls import include, path
from rest_framework.routers import DefaultRouter
from report.api import views as qv

router = DefaultRouter()
router.register(r"report", qv.ReportView)

urlpatterns = [
    path("", include(router.urls)),

    path("rating/waterplace/<int:pk>/",
         qv.Rating_waterplaceAPIView.as_view(),
         name="rating_waterplace"),
#
    path("rating/region/<int:pk>/",
         qv.Rating_regionAPIView.as_view(),
         name="rating_region"),
#

#


]