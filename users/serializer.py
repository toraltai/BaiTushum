from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'occupation', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    # def valdate(self, data):
    #     username = data.get('username', None)
    #
    #     if username is None:
    #         raise serializers.ValidationError(
    #             'An email address is required to log in.'
    #         )
    #
    #     # Вызвать исключение, если не предоставлен пароль.
    #     if password is None:
    #         raise serializers.ValidationError(
    #             'A password is required to log in.'
    #         )
    #     user = authenticate(username=email, password=password)
    #     print(user.email)
    #
    #     if user is None:
    #         raise serializers.ValidationError(
    #             'A user with this email and password was not found.'
    #         )
    #
    #     if not user.is_active:
    #         raise serializers.ValidationError(
    #             'This user has been deactivated.'
    #         )
    #
    #     return {
    #         'email': user.email,
    #         'username': user.username,
    #     }

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password =password)
            if not user:
                raise serializers.ValidationError('wrong')
            attrs['user'] = user
            return attrs
