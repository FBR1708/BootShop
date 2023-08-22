from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.parsers import MultiPartParser
from .serializers import ProductModelSerializer, CategoryModelSerializer, ColorModelSerializer, ProductImageModelSerializer
from .permissions import IsSuperuser, ProductPermission
from .filters import ProductFilter
from .models import *


class ProductModelViewSet(ModelViewSet):
    permission_classes = (IsSuperuser, )
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ProductFilter
