from rest_framework import serializers

from .models import *


class SerializerClient(serializers.ModelSerializer):
    id_credit_spec = serializers.ReadOnlyField(source='id_credit_spec.full_name')

    class Meta:
        model = Client
        # exclude = ['credit_history', 'income_statement', 'contracts', 'report', 'monitoring_report', ]
        fields = "__all__"


class SerializerClientAdmin(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Client
        fields = ['full_name', 'credit_history', 'income_statement', 'contracts', 'report', 'monitoring_report', ]


class SerializerEntity(serializers.ModelSerializer):
    id_credit_spec = serializers.ReadOnlyField(source='id_credit_spec.full_name')

    class Meta:
        model = Entity
        exclude = ['credit_history', 'contracts', 'report', 'monitoring_report', ]


class SerializerEntityAdmin(serializers.ModelSerializer):
    client_company = serializers.ReadOnlyField()
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Client
        fields = ['full_name_director', 'client_company', 'credit_history', 'contracts', 'report',
                  'monitoring_report', 'phone']


class SerializerCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['document']


class SerializerCompanyAdmin(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField()
    inn = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ['company_name', 'inn', 'document']


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

    def get_url(self, instance):
        if instance.file.url.startswith('/media'):
            return f'http://127.0.0.1:8000{instance.file.url}'
        return instance.file.url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['file'] = self.get_url(instance)
        return rep


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

    def get_url(self, instance):
        if instance.image.url.startswith('/media'):
            return f'http://127.0.0.1:8000{instance.image.url}'
        return instance.image.url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self.get_url(instance)
        return rep


class SerializerPropertyAdmin(serializers.ModelSerializer):
    # type = serializers.ReadOnlyField()
    # address = serializers.ReadOnlyField()
    files = FilesSerializer(many=True, read_only=True, )
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        all_data = request.FILES
        property = Property.objects.create(**validated_data)

        Images.objects.bulk_create(
            [Images(property=property, image=image) for image in all_data.getlist('images')]
        )

        Files.objects.bulk_create(
            [Files(property=property, file=f) for f in all_data.getlist('files')]
        )

        return property

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ImagesSerializer(instance.images.all(), many=True).data
        rep['files'] = FilesSerializer(instance.files.all(), many=True).data
        return rep


class SerializerProperty(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['type', 'address']


class SerializerGuarantor(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        exclude = ['income_statement']


class SerializerGuarantorAdmin(serializers.ModelSerializer):
    date = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()

    class Meta:
        model = Guarantor
        fields = ['full_name', 'income_statement']


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
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['id_client'] = SerializerEntity(instance.id_client).data['full_name']
    #     # rep['id_spec'] = SerializerCreditSpecialist(instance.id_spec).data['full_name']
    #     return rep


class SerializersDataKKAdmin(serializers.ModelSerializer):
    class Meta:
        model = DataKK
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
