'''Documentation String'''
from rest_framework.routers import DefaultRouter
from .api.viewsets import NotificationViewSet

router = DefaultRouter()
router.register('notifications', NotificationViewSet, basename='Notification')

urlpatterns = router.urls
