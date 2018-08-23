from rest_framework import permissions


class User(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and (
            request.method in permissions.SAFE_METHODS or
            request.method in ('PUT', 'PATCH') or
            request.user.is_staff or
            view.action in ['logout']
        )

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
