from rest_framework import permissions

class IsStaffOrReadOnly(permissions.IsAdminUser):
    
     def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else :
            return bool(request.user and request.user.is_staff)