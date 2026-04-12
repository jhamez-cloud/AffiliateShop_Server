'''Documentation String'''
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    '''Documentation String'''
    id = django_filters.NumberFilter(field_name="id")
    market = django_filters.CharFilter(field_name="market__slug",lookup_expr="exact")
    category = django_filters.CharFilter(field_name="category__slug",lookup_expr="exact")
    class Meta:
        '''Documentation String'''
        model = Product
        fields = ["id","market","category"]
