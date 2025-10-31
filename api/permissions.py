from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsAdminOrCreateOnly(BasePermission):
    """
    Allow anyone to GET or POST.
    Only admin users can update or delete.
    """
    def has_permission(self, request, view):
        # Allow GET and POST for everyone
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        # Only admins can modify or delete
        return request.user and request.user.is_staff
    
    