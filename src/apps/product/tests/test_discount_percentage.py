from unittest import TestCase

from apps.product.services.discount_percentage import DiscountPercentage


class TestLogicDiscountPercentage(TestCase):

    def test_discount_percentage_50(self) -> None:
        result = DiscountPercentage()(100, 200)
        self.assertEquals(50, result)

    def test_discount_percentage_0(self) -> None:
        result = DiscountPercentage()(0, 50)
        self.assertEquals(0, result)

    def test_discount_percentage_100(self) -> None:
        result = DiscountPercentage()(100, 100)
        self.assertEquals(100, result)
