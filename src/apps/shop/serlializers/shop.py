from rest_framework import serializers

from apps.shop.serlializers.city import CitySerializer


class ShopSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    city = CitySerializer()
    address = serializers.CharField()
    phone = serializers.CharField()
