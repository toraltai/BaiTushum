from rest_framework import serializers

from .models import Client, Company, CreditSpecialist, Entity, MeetConversation, Occupation, Property, Guarantor, TelephoneConversation, DataKK


class SerializerClient(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not instance.is_director:
            representation.pop('client_company')
        return representation


class SerializerEntity(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class SerializerCreditSpecialist(serializers.ModelSerializer):
    class Meta:
        model = CreditSpecialist
        exclude = ['id']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['job_title'] = SerializerOccupation(instance.job_title).data
        return rep

        
class SerializerOccupation(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ['name_job_title']


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