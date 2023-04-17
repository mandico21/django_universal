from typing import Any

from rest_framework import serializers

from apps.product.models import Product, ProductType
from apps.review.serializers import ReviewSerializer
from apps.shop.serlializers.shop import ShopSerializer


class ProductTypeSerializer(serializers.Serializer):
    article = serializers.IntegerField()
    categoryId = serializers.IntegerField(source='category_id')
    brand = serializers.CharField(source='brand.name')
    images = serializers.SerializerMethodField('_get_image')
    name = serializers.CharField()
    description = serializers.CharField()
    basePrice = serializers.DecimalField(max_digits=10, decimal_places=2, source='base_price')
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount = serializers.IntegerField()
    attributes = serializers.SerializerMethodField('_get_attributes')
    info = serializers.SerializerMethodField('_get_info')
    reviews = serializers.SerializerMethodField('_get_review')

    def _get_info(self, obj: ProductType) -> dict[str, Any]:
        return ProductSerializer(obj.products.all(), many=True).data

    def _get_attributes(self, obj: ProductType) -> dict[str, Any]:
        return ProductAttributeSerializer(obj.attributes.order_by('attribute__name').all(), many=True).data

    def _get_image(self, obj: ProductType) -> list[Any]:
        return [str(im.image) for im in obj.images.all()]

    def _get_review(self, obj: ProductType) -> dict[str, Any]:
        return ReviewSerializer(obj.reviews.all(), many=True).data


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


class ProductAttributeSerializer(serializers.Serializer):
    name = serializers.CharField(source='attribute.name')
    meaning = serializers.CharField()
    value = serializers.CharField()
