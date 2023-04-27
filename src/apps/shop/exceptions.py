from django.core.cache import cache
from django.http import HttpResponseRedirect
from rest_framework.exceptions import APIException


class ProductNotFoundException(APIException):
    status_code = 404
    default_detail = 'Товар с данным артикулом не найден'
    default_code = 'product_not_found'


class CategoryNotFoundException(APIException):
    status_code = 404
    default_detail = 'Товары данной категории не найдены'
    default_code = 'product_not_found'


class IncorrectParametersException(APIException):
    status_code = 400
    default_detail = 'Ошибка с параметрами в API'
    default_code = 'incorrect_parameters_error'
