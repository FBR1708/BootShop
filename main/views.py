from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from .models import Product, Category, ProductImage, ProductColor, ProductShop
from .permissions import IsSuperUser, ProductPermission, UserPermission
from .serializers import ProductModelSerializer, CategoryModelSerializer, ProductImageModelSerializer, \
    ProductColorModelSerializer, PostActiveSerializer, UserSerializers, UserActiveSerializers, \
    ProductShopModelSerializer


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


class IsActiveViewSet(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = PostActiveSerializer
    permission_classes = (IsSuperUser,)
    http_method_names = ("patch",)


class UserView(ModelViewSet):
    permission_classes = (UserPermission,)
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserActiveView(ModelViewSet):
    serializer_class = UserActiveSerializers
    queryset = User.objects.all()
    permission_classes = (IsSuperUser,)
    http_method_names = ("patch",)


class ProductShopModelViewSet(ModelViewSet):
    serializer_class = ProductShopModelSerializer
    queryset = ProductShop.objects.all()
    permission_classes = (IsAuthenticated,)
