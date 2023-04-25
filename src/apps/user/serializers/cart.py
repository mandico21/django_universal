from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
