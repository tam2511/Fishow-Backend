from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer,UserDisplaySerializerUpdate,UserADisplaySerializerUpdate
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import CustomUser
from blogs.models import Blog
from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404

#from rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

#from rest_auth.registration.views import SocialConnectView
#from rest_auth.social_serializers import TwitterConnectSerializer
from blogs.api.permissions import IsAuthorOrReadOnly,DjangoObjectPermissionsOrAnonReadOnly

#@list_route(methods['get'],url_path='(?P<username\w+>)')
class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthorOrReadOnly]

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)

class SelectUserAPIView(APIView):
    #permission_classes = [IsAuthorOrReadOnly, DjangoObjectPermissionsOrAnonReadOnly]
    permission_classes = [AllowAny]

    def get(self, request, username):
        user=get_object_or_404(CustomUser, username=username)
        serializer = UserDisplaySerializer(user)
        return Response(serializer.data)


class User_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stats=[]
        stats.append({'count_user':CustomUser.objects.count()})
        return Response(stats)

class UserTopSocialRating(APIView):
    permission_classes = [AllowAny]

    def get(self, request,n,k):
        User = get_user_model()
        users=[]
        Users=User.objects.order_by('-social_rating')
        if len(Users)<int(n)+int(k):
            return Response({'error':'users count lower parameters'})
        Users_nk=Users[n-1:n+k]
        for user in Users_nk:
             users.append({'username':user.username,'email':user.email, 'social_rating':user.social_rating, 'fishing_rating':user.fishing_rating})
        return Response(users)

class UserTopFishingRating(APIView):
    permission_classes = [AllowAny]

    def get(self, request,n,k):
        User = get_user_model()
        users=[]
        Users=User.objects.order_by('-fishing_rating')
        if len(Users)<int(n)+int(k):
            return Response({'error':'users count lower parameters'})
        Users_nk=Users[n-1:n+k]
        for user in Users_nk:
             users.append({'username':user.username,'email':user.email, 'social_rating':user.social_rating, 'fishing_rating':user.fishing_rating})
        return Response(users)

class SubscriptSelectUserAPIView(APIView):

    serializer_class = UserDisplaySerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, username):
        """Remove request.user from the voters queryset of an comment instance."""
        select_user = get_object_or_404(CustomUser, username=username)
        user = request.user

        if select_user in [val for val in user.subscriptions.all()]:
            user.subscriptions.remove(select_user)
            user.save()

            serializer_context = {"request": request}
            serializer = UserDisplaySerializer(user)
            #serializer = self.serializer_class(user, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

    def post(self, request, username):
        """Add request.user to the voters queryset of an comment instance."""
        select_user = get_object_or_404(CustomUser, username=username)
        user = request.user
        if select_user not in [val for val in user.subscriptions.all()]:

            user.subscriptions.add(select_user)
            user.save()

            serializer_context = {"request": request}
            serializer = UserDisplaySerializer(user)
            #serializer = self.serializer_class(user, context=serializer_context)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            serializer_context = {'message':'already_do_it'}
            return Response(serializer_context)

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
            else: break
        return Response(users)

class UpdateProfileView(generics.RetrieveUpdateAPIView):

     queryset = CustomUser.objects.all()
     permission_classes = (IsAuthenticated,)
     serializer_class = UserDisplaySerializerUpdate
     #####lookup_field = 'username'

#      def get_object(self):
#              username = self.kwargs["username"]
#              return get_user_model()

     #get_object_or_404(CustomUser, username=username)
     def get_object(self):
             queryset = self.get_queryset()
             obj = get_object_or_404(queryset, username=self.request.user)
             return obj

     def put(self, request, *args, **kwargs):
             return self.update(request, *args, **kwargs)

class UpdateProfileAvatarView(generics.RetrieveUpdateAPIView):

     queryset = CustomUser.objects.all()
     permission_classes = (IsAuthenticated,)
     serializer_class = UserADisplaySerializerUpdate
     #####lookup_field = 'username'

#      def get_object(self):
#              username = self.kwargs["username"]
#              return get_user_model()

     #get_object_or_404(CustomUser, username=username)
     def get_object(self):
             queryset = self.get_queryset()
             obj = get_object_or_404(queryset, username=self.request.user)
             return obj

     def put(self, request, *args, **kwargs):
             return self.update(request, *args, **kwargs)

     #permission_classes = [IsAuthenticated]

     #def get(self, request):
      #   serializer = UserDisplaySerializer(request.user)
      #   return Response(serializer.data)

# class SubscriptSelectUserAPIView(APIView):
#     #permission_classes = [IsAuthorOrReadOnly, DjangoObjectPermissionsOrAnonReadOnly]
#     #permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]
#
#     def get(self, request, username):
#         user=get_object_or_404(CustomUser, username=username)
#         serializer = UserDisplaySerializer(user)
#         return Response(serializer.data)
#
#     def post(self, request, username):
#         select_user = get_object_or_404(CustomUser, username=username)
#         user = request.user
#         if select_user not in [val for val in user.subscriptions.all()]:
#
#             user.subscriptions.add(select_user)
#             user.save()
#
#             serializer_context = {"request": request}
#             serializer = UserDisplaySerializer(user)
#             #serializer = self.serializer_class(user, context=serializer_context)
#
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         else:
#
#             serializer_context = {'message':'already_do_it'}
#             return Response(serializer_context)

# class UserList(APIView):
#         queryset = get_user_model().objects.all().order_by('social_rating')
#         serializer_class = UserDisplaySerializer
#         permission_classes = [AllowAny]

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter



# class FacebookConnect(SocialConnectView):
#     adapter_class = FacebookOAuth2Adapter





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

