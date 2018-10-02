from rest_framework import permissions


class Runner(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return not request.user.is_anonymous
