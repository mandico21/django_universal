from rest_framework import serializers


class WarehouseSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    # city = CitySerializer()
    cityId = serializers.IntegerField(source='city_id')
    address = serializers.CharField()
    phone = serializers.CharField()
