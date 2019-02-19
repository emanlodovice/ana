from rest_framework.permissions import BasePermission, SAFE_METHODS


class HasReadRecordsPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and \
                   request.user.has_perm('ana.can_access_ana_api_analytics')
        else:
            return True
