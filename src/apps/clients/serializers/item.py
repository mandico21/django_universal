from typing import Any

from rest_framework import serializers

from apps.clients.models.cart import Cart
from apps.clients.services.price_items_cart import PriceItemsCart


class ItemSerializer(serializers.Serializer):
    cartId = serializers.UUIDField(source='cart_id')
    productId = serializers.IntegerField(source='product_id')
    quantity = serializers.IntegerField()


class CartSerializer(serializers.Serializer):
    cartId = serializers.UUIDField(source='client_id')
    items = serializers.SerializerMethodField('_get_items')
    price = serializers.SerializerMethodField('_get_price')

    def _get_items(self, obj: Cart) -> dict[str, Any]:
        return ItemSerializer(obj.items, many=True).data

    def _get_price(self, obj: Cart) -> int:
        return PriceItemsCart()(obj)


class UpdateCartSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class DeleteCartSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

