from rest_framework import serializers
from .models import Rules, TournamentRule




class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'


class TournamentRuleSerializer(serializers.ModelSerializer):
    rules = RulesSerializer(many=True, read_only=True)
    class Meta:
        model = TournamentRule
        fields = '__all__'