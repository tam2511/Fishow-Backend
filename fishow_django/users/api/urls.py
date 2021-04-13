from django.urls import path,re_path
from users.api.views import UpdateProfileView,CurrentUserAPIView,UserTopSocialRating,UserTopFishingRating,UserList,FacebookLogin,SelectUserAPIView,SubscriptSelectUserAPIView,User_count
#from rest_auth.registration.views import (SocialAccountListView, SocialAccountDisconnectView)

urlpatterns = [
    re_path('user_select/(?P<username>.*)/', SelectUserAPIView.as_view(), name='select-user'),
    re_path('user_select/(?P<username>.*)/subscript/', SubscriptSelectUserAPIView.as_view(), name='subscript-select-user'),
    path('user/', CurrentUserAPIView.as_view(), name='current-user'),
    path('count/user/', User_count.as_view(), name='user_count'),
    path('user_top_social_rating/<int:n>/<int:k>/', UserTopSocialRating.as_view(), name='social-user'),
    path('user_top_fishing_rating/<int:n>/<int:k>/', UserTopFishingRating.as_view(), name='fishing-user'),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    re_path('update_user_info/(?P<username>.*)/',UpdateProfileView.as_view(), name='updateuseriinfo')
#    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
#    path('rest-auth/facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
#    path('socialaccounts/',SocialAccountListView.as_view(),name='social_account_list'),
#    path('socialaccounts/(?P<pk>\d+)/disconnect/',SocialAccountDisconnectView.as_view(),name='social_account_disconnect')
]