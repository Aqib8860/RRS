from . import models
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated


class ResturentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.acc_type == "Resturent":
            return True
        else:
            return False


class OfficeUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.acc_type == "Office":
            return True
        else:
            return False
