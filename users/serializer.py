from rest_framework  import serializers
from django.contrib.auth import authenticate
from .models import User, SpecUser, OCCUPATION


class RegisterSpecSerializer(serializers.Serializer):
    '''Регистрация сотрудника'''

    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(min_length=6)
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    occupation = serializers.ChoiceField(choices=OCCUPATION)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь уже существует!')
        return email

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
        ref_name = 'user'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегестрирован!')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Неправильный логин или пароль!")
            attrs['user'] = user
            return attrs



class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name']



# class RegisterClientSerializer(serializers.Serializer):
#     '''Регистрация клиента'''
#
#     email = serializers.EmailField()
#     password = serializers.CharField(min_length=6)
#     password_confirm = serializers.CharField(min_length=6)
#     full_name = serializers.CharField()
#     phone_number = serializers.CharField()
#     address = serializers.CharField()
#
#     def validate(self, attrs):
#         password = attrs.get('password')
#         password_confirm = attrs.pop('password_confirm')
#
#         if password != password_confirm:
#             raise serializers.ValidationError('Пароли не совпадают!')
#         return attrs
#
#     def create(self, validated_data):
#         address = validated_data.pop('address')
#         user = User.objects.create_user(**validated_data)
#         ClientUser.objects.create(user=user, address=address)
#         return user
#
#     def to_representation(self, instance):
#         rep = {}
#         fields = ('email', 'password', 'full_name', 'phone_number')
#         for field in fields:
#             rep[field] = getattr(instance, field)
#         return rep