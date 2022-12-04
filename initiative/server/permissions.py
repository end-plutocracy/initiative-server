from rest_framework import permissions


class CanRetrieveSigneePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class CanRetrieveUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class CanRetrieveSignaturePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.signee.user == request.user
