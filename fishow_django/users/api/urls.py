from django.urls import path,re_path
from users.api.views import CurrentUserAPIView,UserList,UserStatistic,FacebookLogin,FacebookConnect
from rest_auth.registration.views import (SocialAccountListView, SocialAccountDisconnectView)

urlpatterns = [
    path('user/', CurrentUserAPIView.as_view(), name='current-user'),
    path('user_all/', UserList.as_view(), name='all-user'),
    path('user_statistic/',UserStatistic.as_view(), name='statistic-user'),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
    path('socialaccounts/',SocialAccountListView.as_view(),name='social_account_list'),
    path(r'socialaccounts/(?P<pk>\d+)/disconnect/',SocialAccountDisconnectView.as_view(),name='social_account_disconnect')
]