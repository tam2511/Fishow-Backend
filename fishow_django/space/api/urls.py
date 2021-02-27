from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from space.api import views as qv

router = DefaultRouter()
router.register(r"region", qv.RegionView)
router.register(r"waterplace_cost", qv.Waterplace_cost)
router.register(r"waterplace_nature", qv.Waterplace_nature)

urlpatterns = [
    path("", include(router.urls)),
    path("count/waterplace_cost/", qv.Waterplace_cost_count.as_view(), name="waterplace_cost_count"),
    path("count/waterplace_nature/", qv.Waterplace_nature_count.as_view(), name="waterplace_nature_count"),
    path("count/region/", qv.Region_count.as_view(), name="region_count"),
    path("region_list/", qv.Region_list.as_view(), name="region_list"),
    re_path('region_towns/(?P<region>.*)/', qv.SelectRegionAPIView.as_view(), name='select-region'),
]