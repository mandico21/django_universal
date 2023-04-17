from typing import Any

from rest_framework import serializers

from apps.product.models import Product, ProductType
from apps.shop.serlializers.shop import ShopSerializer


class ProductTypeSerializer(serializers.Serializer):
    article = serializers.IntegerField()
    categoryId = serializers.IntegerField(source='category_id')
    name = serializers.CharField()
    description = serializers.CharField()
    basePrice = serializers.DecimalField(max_digits=10, decimal_places=2, source='base_price')
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    info = serializers.SerializerMethodField('_get_info')

    def _get_info(self, obj: ProductType) -> dict[str, Any]:
        return ProductSerializer(obj.products.all(), many=True).data


class ProductTypeListSerializer(serializers.Serializer):
    article = serializers.IntegerField()
    categoryId = serializers.IntegerField(source='category_id')
    name = serializers.CharField()
    basePrice = serializers.DecimalField(max_digits=10, decimal_places=2, source='base_price')
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    count = serializers.SerializerMethodField('_get_count_quantity_product')

    def _get_count_quantity_product(self, obj: ProductType) -> dict[str, Any]:
        return obj.products.count()


class ProductSerializer(serializers.Serializer):
    shop = serializers.SerializerMethodField('_get_shop')
    quantity = serializers.IntegerField()

    def _get_shop(self, obj: Product) -> dict[str, Any]:
        return ShopSerializer(obj.shop).data
