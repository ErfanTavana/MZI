from rest_framework.permissions import BasePermission
from .models import AdminMZI


class UserIsAdminMzi(BasePermission):  # دسترسی تنظیمات هتل
    def has_permission(self, request, view):
        try:
            user = request.user
            AdminMZI.objects.get(user=user, is_admin=True)
            return True
        except:
            return False
