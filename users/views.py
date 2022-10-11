from rest_framework import permissions
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import RegisterClientSerializer, RegistrationAccountSerializer, LogoutSerislizer


class RegistrationAccountAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationAccountSerializer

    def post(self, request):
        data = request.data
        serializer = RegistrationAccountSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLogoutView(APIView):
    serializer_class = LogoutSerislizer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

# class RegistrationClientAPIView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = RegistrationClientSerializer

#     def post(self, request):
#         data = request.data
#         serializer = RegistrationClientSerializer(data=data)

#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

class RegisterClientAPIView(generics.CreateAPIView):
    serializer_class = RegisterClientSerializer
        