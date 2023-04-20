from apps.clients.models.cart import Cart


class PriceItemsCart:

    def __call__(self, cart: Cart) -> int:
        items = cart.items.select_related()
        price = int()
        for item in items:
            price += item.product.product.price * item.quantity
        return price
