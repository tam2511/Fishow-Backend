from django.urls import path,re_path
from users.api.views import CurrentUserAPIView,UserList,UserStatistic

urlpatterns = [
    path('user/', CurrentUserAPIView.as_view(), name='current-user'),
    path('user_all/', UserList.as_view(), name='all-user'),
    path('user_statistic/',UserStatistic.as_view(), name='statistic-user'),
]