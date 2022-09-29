from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

class RegistrationUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'full_name', 'username', 'password']

class RegistrationClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'address','phone_number','password']

    def create(self, validated_data):
        user = User.objects.create_client(**validated_data)

        return user

class RegistrationSpecSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'occupation', 'phone_number','password']

    def create(self, validated_data):
        user = User.objects.create_spec(**validated_data)

        return user

class LogoutSerislizer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad token')