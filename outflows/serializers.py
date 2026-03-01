from rest_framework import serializers
from outflows.models import OutFlow


class OutFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutFlow
        fields = '__all__'
