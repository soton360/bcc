from rest_framework import serializers
from .models import MatchFixture
from team.serializers import TeamSerializer
from django_filters import rest_framework as filters
from django.db.models import Q

class MatchFixtureSerializer(serializers.ModelSerializer):
    team_a = TeamSerializer(read_only=True)
    team_b = TeamSerializer(read_only=True)
    class Meta:
        model = MatchFixture
        fields = '__all__'



class MatchFixtureFilter(filters.FilterSet):
    team = filters.NumberFilter(method='filter_team')

    class Meta:
        model = MatchFixture
        fields = ['tournament']

    def filter_team(self, queryset, name, value):
        return queryset.filter(
            Q(team_a=value) | Q(team_b=value)
        )
