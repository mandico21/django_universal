from typing import Dict

from apps.shop.exceptions import ProductNotFoundException, \
    CategoryNotFoundException, IncorrectParametersException
from apps.shop.models import ProductType
from apps.shop.serializers.product import ProductTypeSerializer, \
    ProductTypeListSerializer


class GetByParameters:

    def __call__(
            self,
            article: int | None,
            category_id: int | None,
            brand_id: int | None
    ) -> Dict:
        if article and category_id and brand_id:
            raise IncorrectParametersException
        elif article:
            return self.get_by_article(article)
        elif category_id:
            return self.get_by_category(category_id)
        elif brand_id:
            return self.get_by_brand(brand_id)
        else:
            raise IncorrectParametersException

    def get_by_article(self, article: int) -> Dict:
        product = ProductType.objects.filter(article=article).first()
        if not product:
            raise ProductNotFoundException
        return ProductTypeSerializer(product).data

    def get_by_category(self, category_id: int) -> Dict:
        products = ProductType.objects.filter(category_id=category_id).all()
        if not products:
            raise CategoryNotFoundException
        return ProductTypeListSerializer(products, many=True).data

    def get_by_brand(self, brand_id: int) -> Dict:
        products = ProductType.objects.filter(brand_id=brand_id).all()
        if not products:
            raise ProductNotFoundException
        return ProductTypeListSerializer(products, many=True).data
