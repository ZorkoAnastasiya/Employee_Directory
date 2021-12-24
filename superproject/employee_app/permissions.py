from rest_framework.permissions import BasePermission

from employee_app.models import User


class IsManagerAuthenticated(BasePermission):
    def has_permission(self, request, view) -> bool:
        """
        Restricts user access rights.
        Access is granted only to "superusers" or users of a specific group.
        """

        if request.user.is_superuser:
            return True
        perm = User.objects.filter(pk=request.user.id, groups__name="Managers").exists()
        return bool(request.user and request.user.is_authenticated and perm)
