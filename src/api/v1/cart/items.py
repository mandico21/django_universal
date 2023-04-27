from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request

from apps.user.serializers.item import CartSerializer, UpdateCartSerializer, \
    DeleteCartSerializer
from apps.user.services.add_product_to_cart import AddProductCart
from apps.user.services.remove_product_to_cart import RemoveProductCart
from apps.user.services.update_product_to_cart import UpdateProductCart
from core.responses import standardize_response


class ItemAPI(CreateAPIView):

    @swagger_auto_schema(
        tags=['Корзина'],
        operation_id='add_product_to_cart',
        operation_summary='Добавить товар в корзину клиента',
        responses={
            200: CartSerializer(),
            404: 'Not Found',
        },
        request_body=UpdateCartSerializer()
    )
    @standardize_response(200)
    def post(self, request: Request, *args, **kwargs) -> dict[str, Any]:
        new_items = UpdateCartSerializer(data=request.data)
        if new_items.is_valid(raise_exception=True):
            return AddProductCart()(**new_items.data)
        return new_items.data

    @swagger_auto_schema(
        tags=['Корзина'],
        operation_id='update_product_to_cart',
        operation_summary='Отредактировать товар в корзине клиента',
        responses={
            200: CartSerializer(),
            404: 'Not Found',
        },
        request_body=UpdateCartSerializer()
    )
    @standardize_response(200)
    def put(self, request: Request, *args, **kwargs) -> dict[str, Any]:
        edit = UpdateCartSerializer(data=request.data)
        if edit.is_valid(raise_exception=True):
            return UpdateProductCart()(**edit.data)
        return edit.data

    @swagger_auto_schema(
        tags=['Корзина'],
        operation_id='remove_product_to_cart',
        operation_summary='Удалить товар из корзины клиента',
        responses={
            200: CartSerializer(),
            404: 'Not Found',
        },
        request_body=DeleteCartSerializer()
    )
    @standardize_response(200)
    def delete(self, request: Request, *args, **kwargs) -> dict[str, Any]:
        delete = DeleteCartSerializer(data=request.data)
        if delete.is_valid(raise_exception=True):
            return RemoveProductCart()(**delete.data)
        return delete.data
