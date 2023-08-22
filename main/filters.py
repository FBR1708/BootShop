from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    name = filters.CharFilter(field_name="name", lookup_expr="iconatains")
    categories = filters.NumberFilter(field_name="categories", lookup_expr="exact")

    class Meta:
        model = Product
        fields = ['name', 'categories']