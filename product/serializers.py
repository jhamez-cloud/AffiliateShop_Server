'''Documentation String'''
from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductSerializer(ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = Product
        fields = "__all__"
