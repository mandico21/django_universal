from typing import Any
from uuid import UUID

from apps.clients.exceptions import CartNotFoundException
from apps.clients.models.cart import Cart, Item
from apps.clients.serializers.item import CartSerializer
from apps.product.exceptions import ProductNotFoundException
from apps.product.models import Product


class AddProductCart:

    def __call__(self, cart_id: UUID | str, product_id: int, quantity: int) -> dict[str, Any]:
        cart = Cart.objects.filter(client_id=cart_id).first()
        if not cart:
            raise CartNotFoundException

        product = Product.objects.filter(id=product_id).first()
        if not product:
            raise ProductNotFoundException

        item = Item.objects.filter(cart_id=cart.id, product_id=product_id).first()
        if item:
            item.quantity = quantity
            item.save()
        else:
            Item.objects.create(cart=cart, product=product, quantity=quantity)
        return CartSerializer(cart).data
