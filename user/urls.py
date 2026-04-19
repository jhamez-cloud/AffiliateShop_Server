'''Documentation String'''
from rest_framework.routers import DefaultRouter
from .api.viewsets import UserViewSet

router = DefaultRouter()
router.register("users",UserViewSet,basename="User")

urlpatterns = router.urls
