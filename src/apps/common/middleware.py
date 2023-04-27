from rest_framework.response import Response


class Process500:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        return self._get_response

    def process_exception(self, request, exc):
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
