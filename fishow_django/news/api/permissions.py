from rest_framework import permissions
from news.models import News
from rest_framework.generics import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class IsAuthorOrReadOnly (permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            view_news(self, request, view, obj)
            return True
        return obj.author == request.user

def view_news(self, request, view, obj):
    if request.user.is_authenticated:
        news=get_object_or_404(News, pk=obj.id)
        user = request.user
        if user not in news.views.all():
            news.views.add(user)
            news.save()

class DjangoObjectPermissionsOrAnonReadOnly(permissions.BasePermission):
    authenticated_users_only = False