from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from djoser.serializers import UserCreateSerializer


class RegistrationUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'full_name', 'username', 'phone_number', 'password']


class RegistrationSpecSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'occupation','phone_number', 'password']

    def create(self, validated_data):
        user = User.objects.create_spec(**validated_data)

        return user
