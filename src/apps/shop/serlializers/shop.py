from rest_framework import serializers

from apps.shop.serlializers.city import CitySerializer


class ShopSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    # city = CitySerializer()
    cityId = serializers.IntegerField(source='city_id')
    address = serializers.CharField()
    phone = serializers.CharField()
