from django.urls import path,re_path
from users.api.views import CurrentUserAPIView,UserList,UserStatistic
from rest_auth.registration.views import VerifyEmailView, RegisterView

urlpatterns = [
    path('user/', CurrentUserAPIView.as_view(), name='current-user'),
    path('user_all/', UserList.as_view(), name='all-user'),
    path('user_statistic/',UserStatistic.as_view(), name='statistic-user'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
         name='account_confirm_email'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(),
             name='account_email_verification_sent'),
]