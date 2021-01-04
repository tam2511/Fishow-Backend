from rest_framework import serializers
from users.models import CustomUser
from blogs.models import Blog

from django.contrib.auth.forms import PasswordResetForm
from allauth.account.forms import ResetPasswordForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from datetime import datetime,timezone
from django.utils.timesince import timesince


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    email = serializers.EmailField()

    password_reset_form_class = ResetPasswordForm

    def get_email_options(self):
        """Override this method to change default e-mail options"""
        return {}

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Invalid e-mail address'))
        return value

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)

class UserDisplaySerializer1(serializers.ModelSerializer):

    rang = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username','email', 'count_blogs', 'count_comments', 'count_report', 'social_rating', 'fishing_rating', 'rang']

    def get_rang(self, instance):
            rang_koef = int(instance.social_rating) + int(instance.fishing_rating)
            if rang_koef<1000:
                return str('Новичок')
            elif rang_koef<10000:
                return str('Любитель')
            elif rang_koef<100000:
                return str('Полупрофессионал')
            elif rang_koef<1000000:
                return str('Профессионал')
            else:
                return str('Мастер')




class UserDisplaySerializer(serializers.ModelSerializer):

    rang = serializers.SerializerMethodField()
    time_from_creations = serializers.SerializerMethodField()
    sort_list_date = serializers.SerializerMethodField()
    sort_list_pop = serializers.SerializerMethodField()
    sort_list_hot = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username','email', 'count_blogs', 'count_comments', 'count_report', 'social_rating', 'fishing_rating', 'rang', 'count_like', 'count_dislike', 'time_from_creations', 'sort_list_date', 'sort_list_pop', 'sort_list_hot','subscriptions']

    def get_rang(self, instance):
            rang_koef = int(instance.social_rating) + int(instance.fishing_rating)
            if rang_koef<1000:
                return str('Новичок')
            elif rang_koef<10000:
                return str('Любитель')
            elif rang_koef<100000:
                return str('Полупрофессионал')
            elif rang_koef<1000000:
                return str('Профессионал')
            else:
                return str('Мастер')

    def get_time_from_creations(self, object):
            created = object.date_joined
            now = datetime.now(timezone.utc)
            time_spend = timesince(created, now)
            return time_spend

    def get_sort_list_date(self, object):
            data = Blog.objects.filter(author=object.id).order_by("-created_at").values('slug')
            return data

    def get_sort_list_pop(self, object):
            data = Blog.objects.filter(author=object.id).order_by("-created_at").values('slug')
            return data

    def get_sort_list_hot(self, object):
            data = Blog.objects.filter(author=object.id).order_by("-created_at").values('slug')
            return data



