from rest_framework import viewsets
from rest_framework import serializers

from .models import Client, Company, CreditSpecialist, MeetConversation, Occupation, Property, Guarantor, TelephoneConversation, DataKK


class SerializerClient(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SerializerCreditSpecialist(serializers.ModelSerializer):
    class Meta:
        model = CreditSpecialist
        fields = '__all__'

        
class SerializerOccupation(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'


class SerializerCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class SerializerProperty(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class SerializerGuarantor(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = '__all__'


class SerializersTelephConvers(serializers.ModelSerializer):
    class Meta:
        model = TelephoneConversation
        fields = '__all__'


class SerializersseetConvers(serializers.ModelSerializer):
    model = MeetConversation
    fields = '__all__'


class SerializersDataKK(serializers.ModelSerializer):
    class Meta:
        model = DataKK
        fields = '__all__'