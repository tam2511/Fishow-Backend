from django.urls import include, path
from rest_framework.routers import DefaultRouter
from report.api import views as qv

router = DefaultRouter()
router.register(r"report", qv.ReportView)

urlpatterns = [
    path("", include(router.urls)),

    path("fishing/", qv.FishingView.as_view(), name='fishing'),

    path("report/<slug:slug>/comments/",
         qv.CommentListAPIView.as_view(),
         name="comment_r-list"),
#
    path("report/<slug:slug>/comment/",
         qv.CommentCreateAPIView.as_view(),
         name="create-comment_r"),
#
    path("comments/<int:pk>/",
         qv.CommentRUDAPIView.as_view(),
         name="comment_r-detail"),
#
    path("comments/<int:pk>/like/",
         qv.CommentLikeAPIView.as_view(),
         name="comment_r-like"),
#
    path("comments/<int:pk>/dislike/",
         qv.CommentDisLikeAPIView.as_view(),
         name="comment_r-dislike"),

    path("report/<int:pk>/like/",
         qv.ReportLikeAPIView.as_view(),
         name="report-like"),

    path("report/<int:pk>/dislike/",
         qv.ReportDisLikeAPIView.as_view(),
         name="report-dislike"),

    path("user/saved/report/", qv.ReportUserSaved.as_view(), name="saved-user"),
    path("user/liked/report/", qv.ReportUserLiked.as_view(), name="liked-user"),
    path("user/created/report/", qv.ReportUserLiked.as_view(), name="liked-user"),
    path("user/liked/report/comment/", qv.ReportUserLiked.as_view(), name="liked-user"),
    path("user/created/report/comment/", qv.ReportUserLiked.as_view(), name="liked-user"),

]