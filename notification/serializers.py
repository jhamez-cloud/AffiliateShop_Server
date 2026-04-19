'''Documentation String'''
from rest_framework.serializers import ModelSerializer
from .models import Notification

class NotificationSerializer(ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = Notification
        fields = "__all__"
