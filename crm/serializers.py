from rest_framework import serializers

from .models import *


class SerializerClient(serializers.ModelSerializer):
    id_credit_spec = serializers.ReadOnlyField(source='id_credit_spec.fullname')

    class Meta:
        model = Client
        exclude = ['credit_history', 'income_statement', 'contracts', 'report', 'monitoring_report', ]


class SerializerClientAdmin(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['credit_history', 'income_statement', 'contracts', 'report', 'monitoring_report', ]


class SerializerEntity(serializers.ModelSerializer):
    id_credit_spec = serializers.ReadOnlyField(source='id_credit_spec.fullname')

    class Meta:
        model = Entity
        exclude = ['credit_history', 'income_statement', 'contracts', 'report', 'monitoring_report', ]


class SerializerEntityAdmin(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['credit_history', 'income_statement', 'contracts', 'report', 'monitoring_report', ]


class SerializerCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['document']


class SerializerCompanyAdmin(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['document']


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class SerializerPropertyAdmin(serializers.ModelSerializer):
    files = FilesSerializer(many=True, read_only=True, )
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


class SerializerProperty(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['type', 'address']


class SerializerGuarantor(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        exclude = ['income_statement']


class SerializerGuarantorAdmin(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = ['income_statement']


class SerializersConvers(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['is_meeting', 'date', 'name', 'time', 'desc']


class SerializersConversFull(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    date = serializers.ReadOnlyField()

    class Meta:
        model = Conversation
        fields = ['name', 'date', 'results_report', 'statistics']


class SerializersDataKK(serializers.ModelSerializer):
    id_spec = serializers.ReadOnlyField(source='id_spec.fullname')

    class Meta:
        model = DataKK
        exclude = ['credit_spec_report', 'committee_decision', 'all_contracts']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id_client'] = SerializerEntity(instance.id_client).data['full_name']
        # rep['id_spec'] = SerializerCreditSpecialist(instance.id_spec).data['full_name']
        return rep


class SerializersDataKKAdmin(serializers.ModelSerializer):
    class Meta:
        model = DataKK
        exclude = ['credit_spec_report', 'committee_decision', 'all_contracts']