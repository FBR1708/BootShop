from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from main.filters import ProductFilter
from main.models import Product, Category, ProductImage, ProductColor
from main.permissions import IsSuperUser, ProductPermission
from main.serializers import ProductModelSerializer, CategoryModelSerializer, ProductImageModelSerializer, \
    ProductColorModelSerializer, PostActiveSerializer


class CategoryClassViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsSuperUser,)


class ProductClassViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductModelSerializer
    permission_classes = (ProductPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageModelSerializer
    permission_classes = (ProductPermission,)
    parser_classes = [MultiPartParser]


class ProductColorViewSet(ModelViewSet):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorModelSerializer
    permission_classes = (ProductPermission,)
    http_method_names = ("get", "post", "delete")


class IsActiveViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PostActiveSerializer
    permission_classes = (IsSuperUser,)
    http_method_names = ("patch",)
