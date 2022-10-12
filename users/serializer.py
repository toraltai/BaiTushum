from random import choices

from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User, ClientUser, SpecUser, OCCUPATION


# регистрация джосера с активацией
class RegistrationUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'full_name', 'phone_number', 'password']


class SpecUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecUser
        fields = ['user', 'occupation']


class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = ['user', 'address']


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
    '''Регистрация клиента'''

    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(min_length=6)
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    address = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

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


class RegisterSpecSerializer(serializers.Serializer):
    '''Регистрация сотрудника'''

    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(min_length=6)
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    occupation = serializers.ChoiceField(choices=OCCUPATION)

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        occupation = validated_data.pop('occupation')
        user = User.objects.create_user(**validated_data)
        SpecUser.objects.create(user=user, occupation=occupation)
        return user

    def to_representation(self, instance):
        rep = {}
        fields = ('email', 'password', 'full_name', 'phone_number')
        for field in fields:
            rep[field] = getattr(instance, field)
        return rep


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'phone_number']

'''
# кастомная регистрация
class RegistrationAccountSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=50)
    password_confirm = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True
    )
    occupation = SpecUserSerializer()

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
        email = validated_data['email']
        password = validated_data['password']
        full_name = validated_data['full_name']
        phone_number = validated_data['phone_number']
        occupation = validated_data['occupation']
        user = User.objects.create_user(email=email, password=password, full_name=full_name, phone_number=phone_number)
        spec_user = SpecUser.objects.create(user=user, occupation=occupation)
        return user


class RegistrationAccountClientSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=50)
    full_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=50)
    password_confirm = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'phone_number', 'password', 'password_confirm', 'address']

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        full_name = validated_data['full_name']
        phone_number = validated_data['phone_number']
        address = validated_data['address']
        user = User.objects.create_user(email=email, password=password, full_name=full_name, phone_number=phone_number)
        client = ClientUser.objects.create(user=user, address=address)
        return user
'''
