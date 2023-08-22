from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import ProductShop, Contact
from users.permissions import UserPermission, IsSuperUser
from users.serializers import UserSerializers, UserActiveSerializers, ProductShopModelSerializer, Contact


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
