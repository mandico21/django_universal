from typing import Any

from _decimal import Decimal
from django.db.models import Sum, F
from rest_framework import serializers

from apps.cart.models import Cart, CartItem


class ItemSerializer(serializers.Serializer):
    cartId = serializers.UUIDField(source='cart_id')
    productId = serializers.IntegerField(source='product_id')
    quantity = serializers.IntegerField()
    amount = serializers.SerializerMethodField('_get_amount')

    def _get_amount(self, obj: CartItem) -> Decimal:
        return obj.product.product.price * obj.quantity


class CartSerializer(serializers.Serializer):
    cartId = serializers.UUIDField(source='client_id')
    items = serializers.SerializerMethodField('_get_items')
    total_amount = serializers.IntegerField()

    def _get_items(self, obj: Cart) -> dict[str, Any]:
        return ItemSerializer(obj.items.select_related('product'), many=True).data

    def _get_price(self, obj: Cart) -> int:
        return obj.items.aggregate(total_amount=Sum(F('product__product__price') * F('quantity')))['total_amount']


class UpdateCartSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class DeleteCartSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    product_id = serializers.IntegerField()
