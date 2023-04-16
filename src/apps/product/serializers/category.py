from typing import Any

from rest_framework import serializers

from apps.product.models import CategoryNode, Category


class CategoryNodeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category = serializers.SerializerMethodField('_get_category')
    parentId = serializers.IntegerField(source='parent_id')
    children = serializers.SerializerMethodField('_get_children')

    def _get_children(self, obj: CategoryNode) -> dict[str, Any]:
        return CategoryNodeSerializer(obj.children.all(), many=True).data

    def _get_category(self, obj: CategoryNode) -> dict[str, Any]:
        return CategorySerializer(obj.category).data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
