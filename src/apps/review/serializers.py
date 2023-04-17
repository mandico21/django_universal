from rest_framework import serializers


class ReviewSerializer(serializers.Serializer):
    name = serializers.CharField()
    dignity = serializers.CharField()
    shortcomings = serializers.CharField()
    comment = serializers.CharField()
