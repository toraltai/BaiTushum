from django.shortcuts import redirect
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import SpecUser, ClientUser
from .serializer import RegistrationAccountSerializer, LogoutSerislizer, SpecUserSerializer, ClientUserSerializer, \
    RegistrationAccountClientSerializer


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


class SpecUserViewAPIView(ModelViewSet):
    serializer_class = SpecUserSerializer
    queryset = SpecUser.objects.all()

    # def perform_create(self, serializer):
    #     print(self.request.user)
    #     serializer.save(user=self.request.user)


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
