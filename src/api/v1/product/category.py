from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.product.models import CategoryNode, Category
from apps.product.serializers.category import CategoryNodeSerializer, CategorySerializer
from core.responses import standardize_response


class ViewCategoryStructure(APIView):

    @swagger_auto_schema(
        tags=['Категории'],
        operation_summary='Получение категорий в структуре',
        operation_description="Метод вернет все категории разделенные по группа",
        responses={200: CategoryNodeSerializer(many=True)},
    )
    @standardize_response(200)
    def get(self, request: Request) -> Response:
        c = CategoryNode.objects.filter(parent_id=None).order_by('id').all()
        return CategoryNodeSerializer(c, many=True).data


class ViewCategory(APIView):

    @swagger_auto_schema(
        tags=['Категории'],
        operation_summary='Получение всех категорий',
        operation_description="Метод вернет все категории",
        responses={200: CategorySerializer(many=True)},
    )
    @standardize_response(200)
    def get(self, request: Request) -> Response:
        c = Category.objects.order_by('id').all()
        return CategorySerializer(c, many=True).data
