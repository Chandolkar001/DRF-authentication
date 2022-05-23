from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone_no')