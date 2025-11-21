from rest_framework import serializers

from role.serializers import RoleSerializer
from team.serializers import TeamSerializer
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ['status']