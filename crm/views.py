from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class APIClient(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = SerializerClient
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(id_credit_spec=self.request.user)

    # def get_serializer_class(self):
    #     occupation = self.request.user.spec_user.occupation
    #     if occupation == 'Кредит.спец':
    #         return SerializerClient
    #     if occupation == 'Кредит.админ':
    #         return SerializerClientAdmin
    #     else:
    #         return redirect('/')


class APIEntity(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = SerializerEntity
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(id_credit_spec=self.request.user)

    # def get_serializer_class(self):
    #     if self.request.user.spec_user.occupation == 'Кредит.спец':
    #         return SerializerEntity
    #     elif self.request.user.spec_user.occupation == 'Кредит.админ':
    #         return SerializerEntityAdmin
    #     else:
    #         return redirect('/')


class APICompany(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = SerializerCompany
    permission_classes = [IsAuthenticated]

    # @decorators.action(['GET'], detail=False)
    # def from_last(self, request):
    #     res = Activity.objects.filter(reverse=False).values()
    #     return Response(ActivitySerializer(res, many=True).data)



# def get_serializer_class(self):
#     if self.request.user.spec_user.occupation == 'Кредит.спец':
#         return SerializerCompany
#     elif self.request.user.spec_user.occupation == 'Кредит.админ':
#         return SerializerCompany
#     else:
#         return redirect('/')


class APIProperty(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = SerializerPropertyAdmin
    permission_classes = [IsAuthenticated]


    # def get_serializer_class(self):
    #     if self.request.user.spec_user.occupation == 'Кредит.спец':
    #         return SerializerProperty
    #     elif self.request.user.spec_user.occupation == 'Кредит.админ':
    #         return SerializerPropertyAdmin
    #     else:
    #         return redirect('/')


class APIGuarantor(ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = SerializerGuarantor
    permission_classes = [IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.request.user.spec_user.occupation == 'Кредит.спец':
    #         return SerializerGuarantor
    #     elif self.request.user.spec_user.occupation == 'Кредит.админ':
    #         return SerializerGuarantorAdmin
    #     else:
    #         return redirect('/')


class APIConvers(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = SerializersConvers
    # permission_classes = [IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.request.user.spec_user.occupation == 'Кредит.спец':
    #         return SerializersConvers
    #     if self.request.user.spec_user.occupation == 'Кредит.админ':
    #         return SerializersConversFull
    #     else:
    #         return redirect('/')


class APIDataKK(ModelViewSet):
    queryset = DataKK.objects.all()
    serializer_class = SerializersDataKK
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(id_spec=self.request.user)

    # def get_serializer_class(self):
    #     if self.request.user.spec_user.occupation == 'Кредит.спец':
    #         return SerializersDataKK
    #     if self.request.user.spec_user.occupation == 'Кредит.админ':
    #         return SerializersDataKKAdmin
    #     else:
    #         return redirect('/')


class ImageAPIView(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class FileAPIView(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

class APIActivity(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    # @decorators.action(['GET'], detail=False)
    # def max_and_min(self, request):
    #     res = Activity.objects.filter()
    #     return Response(ActivitySerializer(res, many=True).data)