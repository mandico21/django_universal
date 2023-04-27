from typing import Any
from uuid import UUID

from django.core.exceptions import ValidationError

from apps.cart.models import Cart, CartItem
from apps.shop.exceptions import ProductNotFoundException
from apps.shop.models import Product
from apps.user.exceptions import CartNotFoundException
from apps.user.serializers.item import CartSerializer


class UpdateProductCart:

    def __call__(
            self,
            cart_id: UUID | str,
            product_id: int,
            quantity: int
    ) -> dict[str, Any]:
        try:
            cart = Cart.objects.filter(client_id=cart_id).first()
            if not cart:
                raise CartNotFoundException
        except ValidationError:
            raise CartNotFoundException

        product = Product.objects.filter(id=product_id).first()
        if not product:
            raise ProductNotFoundException

        item = CartItem.objects.filter(
            cart_id=cart.id,
            product_id=product_id
        ).first()
        if item:
            item.quantity -= quantity
            if item.quantity < 0:
                item.delete()
            else:
                item.save()
        else:
            raise ProductNotFoundException
        return CartSerializer(cart).data
