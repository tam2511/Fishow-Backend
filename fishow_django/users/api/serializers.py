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
from django.db.models import F

index_for_place_social_1 = 10
index_for_place_social_2 = 50
index_for_place_social_3 = 100

index_for_place_fishing_1 = 10
index_for_place_fishing_2 = 50
index_for_place_fishing_3 = 100


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
        fields = ['username','email', 'count_blogs', 'count_comments', 'count_report', 'count_news', 'social_rating', 'fishing_rating', 'rang']

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
    global_rating = serializers.SerializerMethodField()
    rang = serializers.SerializerMethodField()
    time_from_creations = serializers.SerializerMethodField()
    #sort_list_blog_date = serializers.SerializerMethodField()
    #sort_list_blog_pop = serializers.SerializerMethodField()
    #sort_list_blog_hot = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username','email', 'count_blogs', 'count_comments', 'count_report', 'count_news', 'social_rating', 'fishing_rating', 'rang', 'count_like', 'count_dislike', 'time_from_creations', 'global_rating','i_follow', 'country', 'city', 'avatar', 'about', 'tags', 'achievement']

    def get_global_rating(self, instance):
            glob_social_rating = int(instance.social_rating)
            glob_fishing_rating = int(instance.fishing_rating)
            #list = CustomUser.objects.annotate(fieldsum=F('social_rating') + F('fishing_rating')).order_by('-fieldsum')
            list_sr = CustomUser.objects.annotate(fieldsum=F('social_rating')+F('count_blogs')*500 + F('count_news')*500 + F('count_report')*100).order_by('-fieldsum')
            list_fr = CustomUser.objects.annotate(fieldsum=F('fishing_rating')).order_by('-fieldsum')
            index_sr='None'
            for i in range(0,len(list_sr)):
                if instance.email == list_sr[i].email:
                    index_sr=i+1
            place_sr=0
            if index_sr!='None':
                if index_sr<index_for_place_social_1:
                    place_sr=1
                elif index_sr<index_for_place_social_2:
                    place_sr=2
                elif index_sr<index_for_place_social_3:
                    place_sr=3
                else:
                    place_sr=0
            else:
                 place_sr=0

            index_fr='None'
            for i in range(0,len(list_fr)):
                if instance.email == list_fr[i].email:
                    index_fr=i+1
            place_fr=0
            if index_fr!='None':
                if index_fr<index_for_place_fishing_1:
                    place_fr=1
                elif index_fr<index_for_place_fishing_2:
                    place_fr=2
                elif index_fr<index_for_place_fishing_3:
                    place_fr=3
                else:
                    place_fr=0
            else:
                 place_fr=0

            return {'social_rating' :{'index' :index_sr, 'rating' :glob_social_rating, 'place' :place_sr}, 'fishing_rating' :{'index' :index_fr, 'rating' :glob_fishing_rating, 'place' :place_fr}}

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

#     def get_sort_list_blog_date(self, object):
#             data = Blog.objects.filter(author=object.id).order_by("-created_at").values('slug')
#             return data
#
#     def get_sort_list_blog_pop(self, object):
#             data = Blog.objects.filter(author=object.id).order_by("-created_at").values('slug')
#             return data
#
#     def get_sort_list_blog_hot(self, object):
#             data = Blog.objects.filter(author=object.id).order_by("-created_at").values('slug')
#             return data



