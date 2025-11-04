from rest_framework import serializers
from .models import MatchFixture

class MatchFixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchFixture
        fields = '__all__'