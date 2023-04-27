from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.shop.models import CategoryNode, Category
from apps.shop.serializers.category import CategoryNodeSerializer, CategorySerializer
from core.responses import standardize_response


class ViewCategoryStructure(RetrieveAPIView):

    @swagger_auto_schema(
        tags=['Категории'],
        operation_id='view_category_structure',
        operation_summary='Получить структуру категорий',
        responses={200: CategoryNodeSerializer(many=True)},
    )
    @standardize_response(200)
    def get(self, request: Request) -> Response:
        c = CategoryNode.objects.filter(parent_id=None). \
            select_related('category').prefetch_related('childrens').order_by('id').all()
        return CategoryNodeSerializer(c, many=True).data


class ViewCategory(ListAPIView):

    @swagger_auto_schema(
        tags=['Категории'],
        operation_id='view_category',
        operation_summary='Получить все категории',
        responses={
            200: CategorySerializer(many=True)
        },
    )
    @standardize_response(200)
    def get(self, request: Request) -> Response:
        c = Category.objects.order_by('id').all()
        return CategorySerializer(c, many=True).data
