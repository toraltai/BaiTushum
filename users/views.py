from rest_framework import status, generics, permissions,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .models import  User
from .serializer import LoginSerializer, RegisterSpecSerializer, UserSerializer


class RegisterSpecAPIView(generics.CreateAPIView):
    '''Регистрация Спец Кредита'''
    queryset = User.objects.all()
    serializer_class = RegisterSpecSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginApiView(ObtainAuthToken):
    '''Авторизация'''
    serializer_class = LoginSerializer


class LogOutApiView(APIView):
    '''Выход из системы'''
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()
            return Response('Вы успешно разлогинились')
        except Exception as s:
            print('*********', s, '****************')
            return Response(status=403)