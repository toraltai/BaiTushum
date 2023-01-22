from rest_framework import serializers

from .models import *


class SerializerClient(serializers.ModelSerializer):
    id_credit_spec = serializers.ReadOnlyField(source='id_credit_spec.full_name')
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Client
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['id_guarantor'] = SerializerGuarantor(instance.id_guarantor).data['full_name']
    #     rep['id_property'] = SerializerPropertyAdmin(instance.id_property).data['type']
    #     return rep


class SerializerEntity(serializers.ModelSerializer):
    id_credit_spec = serializers.ReadOnlyField(source='id_credit_spec.full_name')
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Entity
        fields = '__all__'


class SerializerCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['field_activity'] = ActivitySerializer(instance.field_activity).data['activites_add']
        return rep


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

    def get_url(self, instance):
        if instance.file.url.startswith('/media'):
            return f'https://bt-back-demo.herokuapp.com{instance.file.url}'
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
            print(instance.image.url)
            return f'https://bt-back-demo.herokuapp.com{instance.image.url}'
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


class SerializerGuarantor(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = '__all__'


class SerializersConvers(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Conversation
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['entity_id'] = SerializerEntity(instance.entity_id).data['full_name_director']
        rep['client_id'] = SerializerClient(instance.client_id).data['full_name']
        return rep


class SerializersDataKK(serializers.ModelSerializer):
    id_spec = serializers.ReadOnlyField(source='id_spec.fullname')
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = DataKK
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id_entity'] = SerializerEntity(instance.id_entity).data['full_name_director']
        rep['id_client'] = SerializerClient(instance.id_client).data['full_name']
        return rep


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'