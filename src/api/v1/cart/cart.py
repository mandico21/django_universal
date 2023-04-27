from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.user.serializers.cart import ClientSerializer
from apps.user.serializers.item import CartSerializer
from apps.user.services.add_cart import AddCart
from apps.user.services.view_cart_client import ViewCartClient
from core.responses import standardize_response


class QueryParamsCart(serializers.Serializer):
    cartId = serializers.CharField()


class CartAPI(APIView):

    @swagger_auto_schema(
        tags=['Корзина'],
        operation_id='create_cart',
        operation_summary='Создать клиента и корзину',
        responses={
            201: ClientSerializer(),
            404: 'Not Found',
        }
    )
    @standardize_response(201)
    def post(self, request: Request, *args, **kwargs) -> dict[str, Any]:
        return AddCart()()

    @swagger_auto_schema(
        tags=['Корзина'],
        query_serializer=QueryParamsCart(),
        operation_id='view_cart',
        operation_summary='Получить корзину клиента',
        responses={
            200: CartSerializer(),
            404: 'Not Found',
        }
    )
    @standardize_response(200)
    def get(self, request: Request, *args, **kwargs) -> dict[str, Any]:
        cart_id = request.query_params['cartId']
        return ViewCartClient()(cart_id)
