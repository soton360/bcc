from rest_framework import serializers
from .models import Tournament

class TournamentSerializer(serializers.ModelSerializer):
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


