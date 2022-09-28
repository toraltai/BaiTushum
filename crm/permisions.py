from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_staff or request.user.is_superuserp)


class IsCreditSpec(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and  request.user.occupation=='Кредит.спец' or request.user.is_superuserp)


class IsCreditAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and  request.user.occupation=='Кредит.админ' or request.user.is_superuserp)
