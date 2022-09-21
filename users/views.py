from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegistrationSerializer,LoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    # serializer_class = RegistrationSerializer

    def post(self, request):
        data = request.data
        print(data)
        serializer = RegistrationSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginSerializerAPIView(ObtainAuthToken):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
#
#
#     def post(self,request):
#         data = request.data
#         print(data)
#         serializer = LoginSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.data)
#         return Response(serializer.data ,
#                         status=status.HTTP_200_OK )
