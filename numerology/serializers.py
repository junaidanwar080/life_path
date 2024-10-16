from rest_framework import serializers
from .models import NumerologyData


class NumerologyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumerologyData
        fields = '__all__'

