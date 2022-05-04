from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and user.is_admin
            or user.is_superuser
        )


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_moderator
        
        
class IsAuthor(BasePermission):
    message = 'Редактировать чужой контент запрещено.'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
