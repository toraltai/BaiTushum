from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import SpecUser, ClientUser
from .serializer import RegistrationAccountSerializer, LogoutSerislizer, SpecUserSerializer, ClientUserSerializer
from django.shortcuts import redirect


class RegistrationAccountAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationAccountSerializer

    def post(self, request):
        data = request.data
        serializer = RegistrationAccountSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return redirect('/users/spec/')


class RegistrationAccountCLientAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationAccountSerializer

    def post(self, request):
        data = request.data
        serializer = RegistrationAccountSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return redirect('/users/client/')


class SpecUserViewAPIView(ModelViewSet):
    serializer_class = SpecUserSerializer
    queryset = SpecUser.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


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

