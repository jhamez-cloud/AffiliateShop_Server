'''Documentation String'''
from rest_framework.serializers import ModelSerializer
from category.serializers import CategorySerializer
from market.serializers import MarketSerializer
from .models import Product

class ProductSerializer(ModelSerializer):
    '''Documentation String'''
    category = CategorySerializer(read_only=True)
    market = MarketSerializer(read_only=True)
    class Meta:
        '''Documentation String'''
        model = Product
        fields = "__all__"
