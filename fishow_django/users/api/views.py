from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer
from users.models import CustomUser
from blogs.models import Blog
from django.contrib.auth import get_user_model

class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)

class UserList(APIView):
    def get(self, request):
        User = get_user_model()
        users = [{'username':user.username,'email':user.email, 'blogs':user.count_blogs, 'comments':user.count_comments,'rating':user.rating} for user in User.objects.all()]
        return Response(users)

class UserStatistic(APIView):
    def get(self, request):
        User = get_user_model()
        users = [{'username':user.username,'blogs':user.count_blogs, 'comments':user.count_comments,'rating':user.rating} for user in User.objects.all()]
        return Response(users)

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

