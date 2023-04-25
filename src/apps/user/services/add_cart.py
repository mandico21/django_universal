from typing import Any

from apps.cart.models import Cart
from apps.user.models.client import Client
from apps.user.serializers.cart import ClientSerializer


class AddCart:

    def __call__(self,) -> dict[str, Any]:
        client = Client.objects.create()
        Cart.objects.create(client=client)

        return ClientSerializer(client).data
