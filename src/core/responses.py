from functools import wraps

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
