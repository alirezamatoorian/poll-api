from rest_framework.permissions import BasePermission


class DeleteAndUpdateOnlyByOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE', 'PUT', 'PATCH']:
            return obj.creator == request.user
        return True
