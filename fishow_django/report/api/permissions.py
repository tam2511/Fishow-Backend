from rest_framework import permissions
from report.models import Report
from rest_framework.generics import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class IsAuthorOrReadOnly (permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            view_report(self, request, view, obj)
            return True
        return obj.author == request.user

def view_report(self, request, view, obj):
    if request.user.is_authenticated:
        report=get_object_or_404(Report, pk=obj.id)
        user = request.user
        if user not in report.views.all():
            report.views.add(user)
            report.save()

class DjangoObjectPermissionsOrAnonReadOnly(permissions.BasePermission):
    authenticated_users_only = False