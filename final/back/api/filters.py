from django_filters import rest_framework as filters
from api.models import Product

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    #min_price
    #max_price
    class Meta:
        model:Product
        fields = ('name')