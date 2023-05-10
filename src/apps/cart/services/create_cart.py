from apps.cart.models import Cart, Status
from apps.user.models import Client


class CreateCart:

    def __call__(self, client_uuid: str | None) -> None:
        if client_uuid is not None:
            client = Client.objects.filter(uuid=client_uuid).first()
            if client is None:
                client = Client.objects.create()
            cart = Cart.objects.filter(
                client=client,
                status=Status.NEW
            ).first()
        else:
            client = Client.objects.create()
            cart = Cart.objects.create(client=client)

        return cart
