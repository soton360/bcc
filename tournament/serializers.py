from rest_framework import serializers
from .models import Tournament
from rules.serializers import RuleSerializer

class TournamentSerializer(serializers.ModelSerializer):
    rules = RuleSerializer(many=True, read_only=True)
    class Meta:
        model = Tournament
        fields = '__all__'

# [
#             'id',
#             'name',
#             'description',
#             'start_date',
#             'end_date',
#             'registration_start',
#             'registration_end',
#             'is_active',
#             'rules',
#         ]


