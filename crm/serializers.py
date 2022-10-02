from rest_framework import serializers

from .models import *


class SerializerClient(serializers.ModelSerializer):
    id_credit_spec = serializers.ReadOnlyField(source='id_credit_spec.fullname')

    class Meta:
        model = Client
        fields = '__all__'


class SerializerEntity(serializers.ModelSerializer):
    id_credit_spec = serializers.ReadOnlyField(source='id_credit_spec.fullname')

    class Meta:
        model = Entity
        exclude = ['id']


class SerializerCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class SerializerProperty(serializers.ModelSerializer):
    files = FilesSerializer(many=True, read_only=True)
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        all_data = request.FILES
        property = Property.objects.create(**validated_data)

        for image in all_data.getlist('images'):
            Images.objects.create(property=property, image=image)

        for f in all_data.getlist('files'):
            Files.objects.create(property=property, file=f)
        return property


class SerializerGuarantor(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = '__all__'


class SerializersConvers(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'


class SerializersDataKK(serializers.ModelSerializer):
    id_spec = serializers.ReadOnlyField(source='id_spec.fullname')

    class Meta:
        model = DataKK
        exclude = ['id']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id_client'] = SerializerEntity(instance.id_client).data['full_name']
        # rep['id_spec'] = SerializerCreditSpecialist(instance.id_spec).data['full_name']
        return rep
