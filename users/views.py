from rest_framework import status, generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  User
from .serializer import RegisterClientSerializer, LogoutSerislizer, RegisterSpecSerializer, UserSerializer


class RegisterClientAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterClientSerializer


class RegisterSpecAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSpecSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLogoutView(APIView):
    serializer_class = LogoutSerislizer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)