from rest_framework.exceptions import APIException


class CartNotFoundException(APIException):
    status_code = 404
    default_detail = 'Корзины с данным ID не было найдено'
    default_code = 'cart_not_found'
