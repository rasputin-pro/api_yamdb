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


class AuthorOrReadOnly(BasePermission):
    """Object-level permission to only allow authors of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """
    message = 'Редактировать чужой контент запрещено.'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
        )
        
        
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated and request.user.is_admin
        )