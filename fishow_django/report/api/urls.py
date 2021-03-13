from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from report.api import views as qv

router = DefaultRouter()
router.register(r"report", qv.ReportView)

urlpatterns = [
    path("", include(router.urls)),

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

    path("report/<slug:slug>/like/",
         qv.ReportLikeAPIView.as_view(),
         name="report-like"),

    path("report/<slug:slug>/dislike/",
         qv.ReportDisLikeAPIView.as_view(),
         name="report-dislike"),

    path("count/report/", qv.Report_count.as_view(), name='report_count'),

    re_path('user_select_reports/created_by/(?P<username>.*)/', qv.ReportUserSelectCreated.as_view(), name="created-blogs-user-select"),
]