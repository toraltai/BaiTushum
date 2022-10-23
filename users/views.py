from rest_framework import status, generics, permissions,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  User
from .serializer import RegisterClientSerializer, LogoutSerializer, RegisterSpecSerializer, UserSerializer
from rest_framework import decorators


class RegisterClientAPIView(generics.CreateAPIView):
# class RegisterClientAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterClientSerializer
    
    # @decorators.action(['GET'], detail=False)
    # def list(self, request):
    #     res = User.objects.all()
    #     return Response(RegisterClientSerializer(res, many=True).data)


class RegisterSpecAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSpecSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)