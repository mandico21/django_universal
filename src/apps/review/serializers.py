from rest_framework import serializers


class ReviewSerializer(serializers.Serializer):
    name = serializers.CharField()
    dignity = serializers.CharField()
    shortcomings = serializers.CharField()
    comment = serializers.CharField()


class CreateReviewSerializer(serializers.Serializer):
    productId = serializers.IntegerField(source='product_id')
    name = serializers.CharField()
    phone = serializers.CharField()
    dignity = serializers.CharField()
    shortcomings = serializers.CharField()
    comment = serializers.CharField()
