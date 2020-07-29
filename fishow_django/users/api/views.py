from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer
from rest_framework.permissions import AllowAny
from users.models import CustomUser
from blogs.models import Blog
from django.contrib.auth import get_user_model

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer

class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)

class UserList(APIView):

    def get(self, request):
        def get_rang(user):
            rang_koef = int(user.social_rating) + int(user.fishing_rating)
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

        User = get_user_model()
        users=[]
        count=0
        for user in User.objects.order_by('social_rating'):
            if count<5:
                users.append({'username':user.username,'email':user.email, 'social_rating':user.social_rating, 'fishing_rating':user.fishing_rating, 'rang':get_rang(user)})
                count=count+1
            else: return
        return Response(users)


# class UserList(APIView):
#         queryset = get_user_model().objects.all().order_by('social_rating')
#         serializer_class = UserDisplaySerializer
#         permission_classes = [AllowAny]

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter



class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter





#sdg

#         User = get_user_model()
#         username = [user.username for user in User.objects.all()]
#         blogs_all = Blog.objects.all()
#         blogs_count_array =[]
#         for user in username:
#             count=0
#             for blog in blogs_all:
#                 if user == blog.author_id:
#                     count=count+1
#             blogs_count_array.append({'username':user,'count':count})

