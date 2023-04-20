from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.product.exceptions import ProductNotFoundException
from apps.product.models import ProductType
from apps.product.serializers.product import ProductTypeSerializer, ProductTypeListSerializer
from core.responses import standardize_response


class ViewProduct(RetrieveAPIView):

    @swagger_auto_schema(
        tags=['Товары'],
        operation_id='view_product',
        operation_summary='Получить товар по артикулу',
        responses={
            200: ProductTypeSerializer(),
            404: "Not Found",
        }
    )
    @standardize_response(200)
    def get(self, request: Request, article: int) -> Response:
        product = ProductType.objects.filter(article=article).first()
        if not product:
            raise ProductNotFoundException
        return ProductTypeSerializer(product).data


class ViewProductByCategory(ListAPIView):

    @swagger_auto_schema(
        tags=['Товары'],
        operation_id='view_product_by_category',
        operation_summary='Получить товары по категории',
        responses={
            200: ProductTypeListSerializer(),
            404: 'Not Found'
        }
    )
    @standardize_response(200)
    def get(self, request: Request, category_id: int) -> None:
        products = ProductType.objects.filter(category_id=category_id).all()
        if not products:
            raise ProductNotFoundException
        return ProductTypeListSerializer(products, many=True).data


class ViewProductByBrand(ListAPIView):

    @swagger_auto_schema(
        tags=['Товары'],
        operation_id='view_product_by_brand',
        operation_summary='Получить товары по бренду',
        responses={
            200: ProductTypeListSerializer(),
            404: 'Not Found'
        }
    )
    @standardize_response(200)
    def get(self, request: Request, brand_id: int) -> None:
        products = ProductType.objects.filter(brand_id=brand_id).all()
        if not products:
            raise ProductNotFoundException
        return ProductTypeListSerializer(products, many=True).data
