from rest_framework import serializers


class CitySerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()
