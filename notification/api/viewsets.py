'''Documentation String'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from account.firebase_auth import FirebaseAuthentication #pylint:disable=e0401
from notification.models import Notification #pylint:disable=e0401
from notification.serializers import NotificationSerializer #pylint:disable=e0401


class IsFirebaseUser(BasePermission):
    '''Documentation String'''
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

class NotificationViewSet(ModelViewSet):
    '''Documentation String'''
    serializer_class = NotificationSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsFirebaseUser]

    def get_queryset(self):
        '''Documentation String'''
        return Notification.objects.filter(
            user=self.request.user
        ).order_by("-created_at")
