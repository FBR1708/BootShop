from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from users.permissions import UserPermission, IsSuperUser
from users.serializers import UserSerializers, UserActiveSerializers


# Create your views here.


class UserView(ModelViewSet):
    permission_classes = (UserPermission,)
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserActiveView(ModelViewSet):
    serializer_class = UserActiveSerializers
    queryset = User.objects.all()
    permission_classes = (IsSuperUser,)
    http_method_names = ("patch",)
