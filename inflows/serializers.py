from rest_framework import serializers
from inflows.models import InFlow


class InFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = InFlow
        fields = '__all__'
