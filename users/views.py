from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .serializer import RegistrationSpecSerializer, RegistrationClientSerializer


class RegistrationSpecAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSpecSerializer

    def post(self, request):
        data = request.data
        serializer = RegistrationSpecSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegistrationClientAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationClientSerializer

    def post(self, request):
        data = request.data
        serializer = RegistrationClientSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
