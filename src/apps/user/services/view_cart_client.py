from typing import Any

from django.core.exceptions import ValidationError

from apps.cart.models import Cart
from apps.user.exceptions import CartNotFoundException
from apps.user.serializers.item import CartSerializer


class ViewCartClient:

    def __call__(self, cart_id: str) -> dict[str, Any]:
        try:
            cart = Cart.objects.filter(
                client_id=cart_id
            ).prefetch_related('items').first()
            if not cart:
                raise CartNotFoundException
        except ValidationError:
            raise CartNotFoundException

        return CartSerializer(cart).data
