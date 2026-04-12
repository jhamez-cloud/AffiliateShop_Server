'''Documentation String'''
from rest_framework import serializers
from .models import Market

class MarketSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = Market
        fields = "__all__"
