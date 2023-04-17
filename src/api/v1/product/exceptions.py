from rest_framework.exceptions import APIException


class ProductNotFoundException(APIException):
    status_code = 404
    default_detail = 'Продукт с данным артикулом не найден'
    default_code = 'product_not_found'
