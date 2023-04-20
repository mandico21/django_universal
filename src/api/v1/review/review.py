from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView

from apps.product.exceptions import ProductNotFoundException
from apps.product.models import ProductType
from apps.review.models import Review
from apps.review.serializers import CreateReviewSerializer
from core.responses import standardize_response


class CreateNewReview(CreateAPIView):

    @swagger_auto_schema(
        tags=['Отзывы'],
        operation_id='create_new_review',
        operation_summary='Получить товары по категории',
        responses={
            201: CreateReviewSerializer(),
            404: 'Not Found',
            400: 'Bad Request',
        },
        request_body=CreateReviewSerializer(),
    )
    @standardize_response(201)
    def post(self, request, *args, **kwargs) -> None:
        new_review = CreateReviewSerializer(data=request.data)
        if new_review.is_valid(raise_exception=True):
            product = ProductType.objects.filter(article=int(request.data['product_id'])).first()
            if not product:
                raise ProductNotFoundException
            Review.objects.create(**new_review.data)
        return new_review.data
