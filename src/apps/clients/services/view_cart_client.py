from typing import Any
from uuid import UUID

from django.core.exceptions import ValidationError

from apps.clients.exceptions import CartNotFoundException
from apps.clients.models.cart import Cart
from apps.clients.serializers.item import CartSerializer


class ViewCartClient:

    def __call__(self, cart_id: str) -> dict[str, Any]:
        try:
            cart = Cart.objects.filter(client_id=cart_id).first()
            if not cart:
                raise CartNotFoundException
        except ValidationError:
            raise CartNotFoundException

        return CartSerializer(cart).data
