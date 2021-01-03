from rest_framework import permissions
from report.models import Report
from rest_framework.generics import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class DjangoObjectPermissionsOrAnonReadOnly(permissions.BasePermission):
    authenticated_users_only = False