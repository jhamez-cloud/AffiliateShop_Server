'''Documentation String'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from django.utils import timezone

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

    def list(self, request, *args, **kwargs):
        """Return notifications for the user.

        If the user has no persisted notifications yet, return a single
        in-memory SYSTEM_ALERT welcome notification so the frontend can
        display it without requiring a DB write from this endpoint.
        """
        qs = self.get_queryset()

        if not qs.exists():
            inst = Notification(
                user=request.user,
                title=Notification.TitleChoices.SYSTEM_ALERT,
                message=(
                    "Welcome to Affiliate Partner! Notifications are now enabled "
                    "for your account — you'll receive updates about orders, "
                    "promotions, and important system alerts here."
                ),
                is_read=False,
                created_at=timezone.now(),
            )
            serializer = self.get_serializer(inst)
            return Response([serializer.data])

        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
