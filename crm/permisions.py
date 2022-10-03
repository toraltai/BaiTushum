from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_staff)


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and  request.user.is_staff or request.user.is_superuser)



class IsCreditAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and  request.user.occupation=='Кредит.админ' or request.user.is_superuserp)
