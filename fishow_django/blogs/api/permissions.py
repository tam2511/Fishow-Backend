from rest_framework import permissions
from blogs.models import Blog
from rest_framework.generics import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class IsAuthorOrReadOnly (permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            view_blog(self, request, view, obj)
            return True
        return obj.author == request.user

def view_blog(self, request, view, obj):
    if request.user.is_authenticated:
        blog=get_object_or_404(Blog, pk=obj.id)
        user = request.user
        if user not in blog.views.all():
            blog.views.add(user)
            blog.save()

class DjangoObjectPermissionsOrAnonReadOnly(permissions.BasePermission):
    authenticated_users_only = False