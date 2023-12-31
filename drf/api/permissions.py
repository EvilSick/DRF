from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and \
            request.user.is_superuser
        )
    
class IsSuperUSerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and \
              request.user.is_superuser
    
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool (
            request.user.is_authenticated and request.user.is_superuser or \
            request.user.is_authenticated and obj.author == request.user
        )