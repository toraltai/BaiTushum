from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User, ClientUser, SpecUser


# регистрация джосера с активацией
class RegistrationUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'full_name', 'phone_number', 'password']


# кастомная регистрация
class RegistrationAccountSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'phone_number', 'password', 'password_confirm', 'occupation']

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
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


class RegisterClientSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        address = validated_data.pop('address')
        user = User.objects.create_user(**validated_data)
        ClientUser.objects.create(user=user, address=address)
        return user
    
    def to_representation(self, instance):
        rep = {}
        fields = ('email', 'password', 'full_name', 'phone_number')
        for field in fields:
            rep[field] = getattr(instance, field)
        return rep