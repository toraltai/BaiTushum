from rest_framework import permissions
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import SpecUser, ClientUser, User
from .serializer import RegisterClientSerializer, LogoutSerislizer, SpecUserSerializer, ClientUserSerializer, \
    RegisterSpecSerializer, UserSerializer


class RegisterClientAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterClientSerializer


class RegisterSpecAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSpecSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SpecUserViewAPIView(ModelViewSet):
    serializer_class = SpecUserSerializer
    queryset = SpecUser.objects.all()


class ClientUserViewAPIView(ModelViewSet):
    serializer_class = ClientUserSerializer
    queryset = ClientUser.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class UserLogoutView(APIView):
    serializer_class = LogoutSerislizer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
class RegistrationAccountAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationAccountSerializer

    def post(self, request):
        data = request.data
        serializer = RegistrationAccountSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegistrationAccountCLientAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationAccountClientSerializer

    def post(self, request):
        data = request.data
        serializer = RegistrationAccountClientSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

'''
