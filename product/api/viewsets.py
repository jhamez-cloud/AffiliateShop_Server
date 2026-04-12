'''Documentation String'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from product.serializers import ProductSerializer #pylint:disable=e0401
from product.models import Product #pylint:disable=e0401
from product.filters import ProductFilter #pylint:disable=e0401

class ProductViewset(ModelViewSet):
    '''Documentation String'''
    queryset = Product.objects.select_related("category","market").all()

    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [AllowAny]
    filterset_class = ProductFilter

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {"market__slug":["exact"]}
