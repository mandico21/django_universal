from typing import Any

from rest_framework import serializers

from apps.guide.serlializers.warehouse import WarehouseSerializer
from apps.shop.models import Product, ProductType
from apps.user.serializers import ReviewSerializer


class ProductTypeSerializer(serializers.Serializer):
    article = serializers.IntegerField()
    categoryId = serializers.IntegerField(source='category_id')
    brand = serializers.CharField()
    images = serializers.SerializerMethodField('_get_image')
    poster = serializers.CharField(source='img_path')
    name = serializers.CharField()
    description = serializers.CharField()
    basePrice = serializers.DecimalField(max_digits=10, decimal_places=2, source='base_price')
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount = serializers.IntegerField()
    attributes = serializers.SerializerMethodField('_get_attributes')
    info = serializers.SerializerMethodField('_get_info')
    reviews = serializers.SerializerMethodField('_get_review')

    def _get_info(self, obj: ProductType) -> dict[str, Any]:
        return ProductSerializer(obj.products.select_related('warehouse'), many=True).data

    def _get_attributes(self, obj: ProductType) -> dict[str, Any]:
        return ProductAttributeSerializer(obj.attributes.select_related('attribute', 'value'), many=True).data

    def _get_image(self, obj: ProductType) -> list[Any]:
        return [str(im.url_path) for im in obj.images.all()]

    def _get_review(self, obj: ProductType) -> dict[str, Any]:
        return ReviewSerializer(obj.reviews, many=True).data

    # def _get_brand(self, obj: ProductType) -> str:
    #     return obj.brand.name if obj.brand else None


class ProductTypeListSerializer(serializers.Serializer):
    article = serializers.IntegerField()
    categoryId = serializers.IntegerField(source='category_id')
    poster = serializers.CharField(source='img_path')
    name = serializers.CharField()
    basePrice = serializers.DecimalField(max_digits=10, decimal_places=2, source='base_price')
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount = serializers.IntegerField()
    count = serializers.SerializerMethodField('_get_count_quantity_product')

    def _get_count_quantity_product(self, obj: ProductType) -> int:
        return obj.products.count()


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    warehouse = serializers.SerializerMethodField('_get_shop')
    quantity = serializers.IntegerField()

    def _get_shop(self, obj: Product) -> dict[str, Any]:
        return WarehouseSerializer(obj.warehouse).data


class ProductAttributeSerializer(serializers.Serializer):
    name = serializers.CharField(source='attribute')
    meaning = serializers.CharField()
    value = serializers.CharField()
