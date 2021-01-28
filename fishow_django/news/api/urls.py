from django.urls import include, path
from rest_framework.routers import DefaultRouter
from news.api import views as qv

router = DefaultRouter()
router.register(r"news", qv.NewsView)

urlpatterns = [
    path("", include(router.urls)),

    path("news/<slug:slug>/comments/",
         qv.CommentListAPIView.as_view(),
         name="comment_n-list"),
#
    path("news/<slug:slug>/comment/",
         qv.CommentCreateAPIView.as_view(),
         name="create-comment_n"),
#
    path("comments/<int:pk>/",
         qv.CommentRUDAPIView.as_view(),
         name="comment_n-detail"),
#
    path("comments/<int:pk>/like/",
         qv.CommentLikeAPIView.as_view(),
         name="comment_n-like"),
#
    path("comments/<int:pk>/dislike/",
         qv.CommentDisLikeAPIView.as_view(),
         name="comment_n-dislike"),

    path("news/<slug:slug>/like/",
         qv.NewsLikeAPIView.as_view(),
         name="news-like"),

    path("news/<slug:slug>/dislike/",
         qv.NewsDisLikeAPIView.as_view(),
         name="news-dislike"),

    path("count/news/", qv.News_count.as_view(), name="news_count"),

]