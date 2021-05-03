from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from blogs.api import views as qv

router = DefaultRouter()
router.register(r"blogs", qv.BlogViewSet)
urlpatterns = [
    path("", include(router.urls)),

    path("blogs/<slug:slug>/comments/",
         qv.CommentListAPIView.as_view(),
         name="comments-list"),

    path("blogs/<slug:slug>/comment/",
         qv.CommentCreateAPIView.as_view(),
         name="create-comments"),

    path("comments/<int:pk>/",
         qv.CommentRUDAPIView.as_view(),
         name="comment-detail"),

    path("comments/<int:pk>/like/",
         qv.CommentLikeAPIView.as_view(),
         name="comment-like"),

    path("comments/<int:pk>/dislike/",
         qv.CommentDisLikeAPIView.as_view(),
         name="comment-dislike"),

    path("blogs/<slug:slug>/like/",
         qv.BlogLikeAPIView.as_view(),
         name="blog-like"),

    path("blogs/<slug:slug>/dislike/",
         qv.BlogDisLikeAPIView.as_view(),
         name="blog-dislike"),

    path("blogs/<slug:slug>/save/",
         qv.BlogSaveAPIView.as_view(),
         name="blog-save"),

    path("count/blogs/", qv.Blogs_count.as_view(), name='blogs_count'),
    path("user/saved/blogs/", qv.BlogUserSaved.as_view(), name="saved-blogs-user"),
    path("user/liked/blogs/", qv.BlogUserLiked.as_view(), name="liked-blogs-user"),
    path("user/created/blogs/", qv.BlogUserCreated.as_view(), name="created-blogs-user"),
    path("user/liked/blogs/comment/", qv.BlogCommentUserLiked.as_view(), name="liked-blogs-comments-user"),
    path("user/created/blogs/comment/", qv.BlogCommentUserCreated.as_view(), name="created-blogs-comments-user"),

    re_path('user_select_blogs/created_by/(?P<username>.*)/', qv.BlogUserSelectCreated.as_view(), name="created-blogs-user-select"),

    path("blogs_fresh/", qv.BlogFresh.as_view(), name="blogs-fresh"),
    path("blogs_best/", qv.BlogBest.as_view(), name="blogs-best"),
    path("blogs_hot/", qv.BlogHot.as_view(), name="blogs-hot"),
    path("blogs_nonviewed/", qv.BlogNonviewed.as_view(), name="blogs-nonviewed"),
    path("blogs_recommend/", qv.BlogNonviewed.as_view(), name="blogs-nonviewed"),
]
