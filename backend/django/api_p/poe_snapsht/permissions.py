from rest_framework import permissions


class IsOwnerOrCreateOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ('post', 'POST'):
            return True

        return obj.account.user == request.user