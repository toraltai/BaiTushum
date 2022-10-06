from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User, SpecUser


class RegistrationUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'password']


class RegistrationClientSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True
    )

    class Meta:
        model = SpecUser
        fields = ['email', 'full_name', 'password', 'password_confirm']

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class RegistrationSpecSerializer(serializers.ModelSerializer):
    # password_confirm = serializers.CharField(
    #     max_length=128,
    #     min_length=6,
    #     write_only=True
    # )

    class Meta:
        model = SpecUser
        fields = '__all__'

    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     password_confirm = attrs.pop('password_confirm')
    #
    #     if password != password_confirm:
    #         raise serializers.ValidationError('Пароли не совпадают!')
    #     return attrs

    def create(self, validated_data):
        print(validated_data)
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = User.objects.create_user(email=email, password=password)
        self.validated_data['user'] = user
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
