from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework import decorators
from .serializers import *
from .models import Client, Company, CreditSpecialist, Entity, Occupation, Property, Guarantor, TelephoneConversation, DataKK
from .permisions import IsCreditSpec,IsCreditAdmin


class APIClient(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = SerializerClient


class APIEntity(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = SerializerEntity
        

class APICreditSpecialist(ModelViewSet):
    queryset = CreditSpecialist.objects.all()
    serializer_class = SerializerCreditSpecialist


class APIOccupation(ModelViewSet):
    permission_classes = [IsCreditSpec,]
    queryset = Occupation.objects.all()
    serializer_class = SerializerOccupation


class APICompany(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = SerializerCompany


class APIProperty(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = SerializerProperty


class APIGuarantor(ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = SerializerGuarantor


class APITelephConvers(ModelViewSet):
    queryset = TelephoneConversation.objects.all()
    fields = '__all__'


class APIMeetConvers(ModelViewSet):
    queryset = MeetConversation.objects.all()
    fields = '__all__'


class APIDataKK(ModelViewSet):
    queryset = DataKK.objects.all()
    serializer_class = SerializersDataKK
    # permission_classes = IsAdminUser
