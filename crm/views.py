from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .permisions import IsStaff
from .serializers import *


class APIClient(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = SerializerClient
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(id_credit_spec=self.request.user)

    # def get_serializer_class(self):
    #     if self.request.user.specuser.occupation == 'Кредит.спец':
    #         return SerializerClient
    #     else:
    #         return SerializerClientAdmin


class APIEntity(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = SerializerEntity
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(id_credit_spec=self.request.user)

    # def get_serializer_class(self):
    #     if self.request.user.specuser.occupation == 'Кредит.спец':
    #         return SerializerEntity
    #     else:
    #         return SerializerEntityAdmin


class APICompany(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = SerializerCompany
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_serializer_class(self):
    #     if self.request.user.specuser.occupation == 'Кредит.спец':
    #         return SerializerCompany
    #     else:
    #         return SerializerCompanyAdmin


class APIProperty(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = SerializerPropertyAdmin
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # def get_serializer_class(self):
    #     if self.request.user.occupation == 'Кредит.спец':
    #         return SerializerProperty
    #     else:
    #         return SerializerPropertyAdmin
    #


class APIGuarantor(ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = SerializerGuarantor
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_serializer_class(self):
    #     if self.request.user.specuser.occupation == 'Кредит.спец':
    #         return SerializerGuarantor
    #     else:
    #         return SerializerGuarantorAdmin


class APIConvers(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = SerializersConvers
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_serializer_class(self):
    #     if self.request.user.specuser.occupation == 'Кредит.спец':
    #         return SerializersConvers
    #     else:
    #         return SerializersConversFull


class APIDataKK(ModelViewSet):
    queryset = DataKK.objects.all()
    serializer_class = SerializersDataKK
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(id_spec=self.request.user)

    # def get_serializer_class(self):
    #     if self.request.user.specuser.occupation == 'Кредит.спец':
    #         return SerializersDataKK
    #     else:
    #         return SerializersDataKKAdmin
