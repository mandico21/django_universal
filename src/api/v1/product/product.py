from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.shop.serializers.product import ProductTypeSerializer
from apps.shop.services.get_by_parametrs import GetByParameters
from core.responses import standardize_response


class ViewProduct(APIView):

    @swagger_auto_schema(
        tags=['Товары'],
        manual_parameters=[
            openapi.Parameter(
                'article',
                openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False
            ),
            openapi.Parameter(
                'categoryId',
                openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False
            ),
            openapi.Parameter(
                'brandId',
                openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False
            ),
        ],
        operation_id='view_product',
        operation_summary='Получить товар по параметру',
        responses={
            200: ProductTypeSerializer(),
            404: 'Not Found',
            400: 'Bad Request'
        },
    )
    @standardize_response(200)
    def get(self, request: Request) -> dict:
        article = request.query_params.get('article', None)
        category_id = request.query_params.get('categoryId', None)
        brand_id = request.query_params.get('brandId', None)
        return GetByParameters()(article, category_id, brand_id)
