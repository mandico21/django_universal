from typing import Any
from uuid import UUID

from apps.cart.models import Cart, CartItem
from apps.user.exceptions import CartNotFoundException, QuantityLessEqualZeroException
from apps.user.serializers.item import CartSerializer
from apps.shop.exceptions import ProductNotFoundException
from apps.shop.models import Product


class AddProductCart:

    def __call__(self, cart_id: UUID | str, product_id: int, quantity: int) -> dict[str, Any]:
        cart = Cart.objects.filter(client_id=cart_id).first()
        if not cart:
            raise CartNotFoundException

        product = Product.objects.filter(id=product_id).first()
        if not product:
            raise ProductNotFoundException

        item = CartItem.objects.filter(cart_id=cart.id, product_id=product_id).first()
        if item:
            if quantity <= 0:
                raise QuantityLessEqualZeroException
            item.quantity = quantity
            item.save()
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        return CartSerializer(cart).data
