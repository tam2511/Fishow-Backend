from django.shortcuts import render

# Create your views here.
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

from allauth.account.views import PasswordResetView

from django.conf import settings
from django.dispatch import receiver
from django.http import HttpRequest
from django.middleware.csrf import get_token

class DefaultAccountAdapterCustom(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        try:
            context['activate_url'] = settings.URL_FRONT + \
                'account-confirm-email/' + context['key'] + '/'
        except:
            pass
#         context['password_reset_url'] = settings.URL_FRONT + \
#             'api/rest-auth/password/reset/confirm/'+ context['token'] + '/'
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
