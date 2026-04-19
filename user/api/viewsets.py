'''Documentation String'''
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from user.models import UserProfile #pylint:disable=e0401
from user.serializers import UserSerializer #pylint:disable=e0401

class UserViewSet(viewsets.ModelViewSet):
    '''Documentation String'''
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
