from rest_framework import serializers

from .models import Client, Company, CreditSpecialist, Entity, MeetConversation, Occupation, Property, Guarantor, \
    TelephoneConversation, DataKK, Files


class SerializerClient(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


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


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'


class SerializerProperty(serializers.ModelSerializer):
    files = FilesSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        files = requests.FILES
        property = Property.objects.create(**validated_data)

        for file in files.getlist('files'):
            Files.objects.create(property=property, file=file)

        return property


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
