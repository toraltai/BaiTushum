from rest_framework import status, generics, permissions,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
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


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            print(dir(token))
            token.delete()
            # t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

