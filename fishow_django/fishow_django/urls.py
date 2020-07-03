from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_framework.authtoken import views

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

    path('api/',
         include('users.api.urls')),

    path('api/',
         include('blogs.api.urls')),

    path('api/',
         include('prediction.api.urls')),

    path('api/',
         include('report.api.urls')),

    path('api-auth/',
         include('rest_framework.urls')),

    path('api/rest-auth/',
         include("rest_auth.urls")),

    path('api/rest-auth/registration/',
         include('rest_auth.registration.urls')),

    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
         name='account_confirm_email'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(),
             name='account_email_verification_sent'),

    re_path(r"^.*$", IndexTemplateView.as_view(), name='entry-point')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
