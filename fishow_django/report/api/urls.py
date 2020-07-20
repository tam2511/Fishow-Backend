from django.urls import include, path
from rest_framework.routers import DefaultRouter
from report.api import views as qv

router = DefaultRouter()
router.register(r"report", qv.ReportView)

urlpatterns = [
    path("", include(router.urls)),

#     path("blogs/<slug:slug>/comments/",
#          qv.CommentListAPIView.as_view(),
#          name="comments-list"),
#
#     path("blogs/<slug:slug>/comment/",
#          qv.CommentCreateAPIView.as_view(),
#          name="create-comments"),
#
#     path("comments/<int:pk>/",
#          qv.CommentRUDAPIView.as_view(),
#          name="comment-detail"),
#
#     path("comments/<int:pk>/like/",
#          qv.CommentLikeAPIView.as_view(),
#          name="comment-like"),
#
#     path("comments/<int:pk>/dislike/",
#          qv.CommentDisLikeAPIView.as_view(),
#          name="comment-dislike"),

    path("report/<int:pk>/like/",
         qv.ReportLikeAPIView.as_view(),
         name="report-like"),

    path("report/<int:pk>/dislike/",
         qv.ReportDisLikeAPIView.as_view(),
         name="report-dislike"),

]