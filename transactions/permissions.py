from rest_framework import permissions

class TransactionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        
        if request.user.role == 'analyst' and request.method in ['GET', 'POST']:
            return True
        
        if request.user.role == 'viewer' and request.method == 'GET':
            return True

        return False