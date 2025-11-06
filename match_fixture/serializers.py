from rest_framework import serializers
from .models import MatchFixture
from team.serializers import TeamSerializer

class MatchFixtureSerializer(serializers.ModelSerializer):
    team_a = TeamSerializer(read_only=True)
    team_b = TeamSerializer(read_only=True)
    class Meta:
        model = MatchFixture
        fields = '__all__'

