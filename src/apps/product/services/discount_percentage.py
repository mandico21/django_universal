from decimal import Decimal


class DiscountPercentage:

    def __call__(self, part: int | float | Decimal, whole: int | float | Decimal) -> int:
        if part and whole:
            return int((part / whole) * 100)
        return 0
