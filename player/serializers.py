from rest_framework import serializers

from role.models import Role
from role.serializers import RoleSerializer
from team.models import Team
from team.serializers import TeamSerializer
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    team = TeamSerializer(read_only=True)

    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), write_only=True, source='role'
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), write_only=True, source='team'
    )
    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ['status']