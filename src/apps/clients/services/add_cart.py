from typing import Any

from apps.clients.models.cart import Cart
from apps.clients.models.client import Client
from apps.clients.serializers.cart import ClientSerializer


class AddCart:

    def __call__(self,) -> dict[str, Any]:
        client = Client.objects.create()
        Cart.objects.create(client=client)

        return ClientSerializer(client).data
