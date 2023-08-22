from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField

from rest_framework.serializers import ModelSerializer


class UserSerializers(ModelSerializer):
    confirm_password = CharField(max_length=50, read_only=True)

    class Meta:
        model = User
        fields = 'id', 'name', 'username', 'password', 'confirm_password', 'email'

    def create(self, validated_data):
        password = validated_data['password']
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise ValidationError('Invalid User')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.confirm_password = validated_data.get('confirm_password', instance.confirm_password)
        instance.name = validated_data.get('first_name', instance.name)
        instance.username = validated_data.get('last_name', instance.username)
        instance.email = validated_data.get('email', instance.email)

        new_password = validated_data.get('password')
        if new_password:
            instance.password = make_password(new_password)

        instance.save()
        return instance


class UserActiveSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'is_staff'