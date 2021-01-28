from django.urls import include, path
from rest_framework.routers import DefaultRouter
from space.api import views as qv

router = DefaultRouter()
router.register(r"region", qv.Region)
router.register(r"waterplace_cost", qv.Waterplace_cost)
router.register(r"waterplace_nature", qv.Waterplace_nature)

urlpatterns = [
    path("", include(router.urls)),


]