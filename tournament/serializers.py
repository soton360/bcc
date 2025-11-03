from rest_framework import serializers
from .models import Tournament, TournamentRuleTitle, TournamentRule


class TournamentRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentRule
        fields = ['rule']


class TournamentRuleTitleSerializer(serializers.ModelSerializer):
    rules = TournamentRuleSerializer(many=True)

    class Meta:
        model = TournamentRuleTitle
        fields = ['title', 'rules']


class TournamentSerializer(serializers.ModelSerializer):
    tournament_rules = TournamentRuleTitleSerializer(many=True)

    class Meta:
        model = Tournament
        fields = '__all__'
