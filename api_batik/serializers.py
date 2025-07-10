from rest_framework import serializers
from .models import KainBatik

class KainBatikSerializer(serializers.ModelSerializer):
    class Meta:
        model = KainBatik
        fields = '__all__'