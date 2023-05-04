from apps.shop.services.discount_percentage import DiscountPercentage


class TestLogicDiscountPercentage:

    def test_discount_percentage_50(self) -> None:
        result = DiscountPercentage()(100, 200)
        assert result == 50

    def test_discount_percentage_0(self) -> None:
        result = DiscountPercentage()(0, 50)
        assert result == 0

    def test_discount_percentage_100(self) -> None:
        result = DiscountPercentage()(100, 100)
        assert result == 100
