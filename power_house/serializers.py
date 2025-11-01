from rest_framework import serializers
from .models import PowerHouse

class PowerHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerHouse
        fields = '__all__'