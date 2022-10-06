from djoser.serializers import UserCreateSerializer, ActivationSerializer, SendEmailResetSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User
class RegistrationUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'username', 'full_name', 'address', 'phone_number', 'password']


class RegistrationClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'address', 'phone_number', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user


class RegistrationSpecSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'occupation', 'phone_number', 'password']

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
