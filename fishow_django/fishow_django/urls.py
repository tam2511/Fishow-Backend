from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_auth.views import PasswordResetConfirmView,PasswordResetView
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/register/',
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url='/',
         ), name='django_registration_register'),

    path("accounts/",
         include("django_registration.backends.one_step.urls")),

    path('accounts/',
         include('django.contrib.auth.urls')),

     path('account/',
          include('allauth.urls')),

    path('api/',
         include('users.api.urls')),

    path('api/',
         include('blogs.api.urls')),

    path('api/',
         include('space.api.urls')),

    path('api/',
         include('prediction.api.urls')),

    path('api/',
         include('report.api.urls')),

    path('api/',
         include('news.api.urls')),

    path('api-auth/',
         include('rest_framework.urls')),

    path('api/rest-auth/',
         include("rest_auth.urls")),

    path('api/rest-auth/registration/',
         include('rest_auth.registration.urls')),

#     path(r'api-token-auth/', obtain_jwt_token),
#     path(r'api-token-refresh/', refresh_jwt_token),
#     path(r'^api-token-verify/', verify_jwt_token),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
         name='account_confirm_email'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(),
             name='account_email_verification_sent'),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),

    re_path(r"^.*$", IndexTemplateView.as_view(), name='entry-point')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
