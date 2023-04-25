from rest_framework import serializers


class ReviewSerializer(serializers.Serializer):
    name = serializers.CharField()
    dignity = serializers.CharField()
    shortcomings = serializers.CharField()
    comment = serializers.CharField()


class CreateReviewSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    name = serializers.CharField()
    phone = serializers.CharField()
    dignity = serializers.CharField()
    shortcomings = serializers.CharField()
    comment = serializers.CharField()
