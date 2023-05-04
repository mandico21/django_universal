from rest_framework import serializers

from apps.user.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'uuid',
            'first_name',
            'last_name',
            'middle_name',
            'phone',
            'email',
        )
