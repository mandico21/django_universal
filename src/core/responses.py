from functools import wraps

from rest_framework.exceptions import APIException
from rest_framework.response import Response


def standardize_response(status_code: int = 500):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result_func = func(*args, **kwargs)
            response = {
                'status': True,
                'status_code': status_code,
                'result': result_func,
                'error': []
            }
            return Response(response, status=status_code)

        return wrapper

    return decorator


def custom_exception_handler(exc: APIException, context):
    response = {
        'status': False,
        'status_code': exc.status_code,
        'result': [],
        'error': {
            'code': exc.default_code,
            'message': exc.detail
        }
    }

    return Response(response, status=exc.status_code)


def custom_exception_error(exc: APIException, context):
    response = {
        'status': False,
        'status_code': '',
        'result': [],
        'error': {
            'code': '',
            'message': ''
        }
    }

    return Response(response, status=exc.status_code)
