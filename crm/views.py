from rest_framework.viewsets import ModelViewSet

from .serializers import *


class APIClient(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = SerializerClient

    def perform_create(self, serializer):
        serializer.save(id_credit_spec=self.request.user)


class APIEntity(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = SerializerEntity

    def perform_create(self, serializer):
        serializer.save(id_credit_spec=self.request.user)


class APICompany(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = SerializerCompany


class APIProperty(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = SerializerProperty


class APIGuarantor(ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = SerializerGuarantor


class APIConvers(ModelViewSet):
    queryset = Conversation.objects.all()
    fields = '__all__'


class APIDataKK(ModelViewSet):
    queryset = DataKK.objects.all()
    serializer_class = SerializersDataKK

    def perform_create(self, serializer):
        serializer.save(id_spec=self.request.user)
