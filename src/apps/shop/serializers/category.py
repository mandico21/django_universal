from typing import Any

from rest_framework import serializers

from apps.shop.models import CategoryNode, Category


class CategoryNodeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category = serializers.SerializerMethodField('_get_category')
    parentId = serializers.IntegerField(source='parent_id')
    childrens = serializers.SerializerMethodField('_get_childrens')

    def _get_childrens(self, obj: CategoryNode) -> dict[str, Any]:
        return CategoryNodeSerializer(obj.childrens.all(), many=True).data

    def _get_category(self, obj: CategoryNode) -> dict[str, Any]:
        return CategorySerializer(obj.category).data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
