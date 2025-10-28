from rest_framework import status
from rest_framework.response import Response

from api.views import CustomModelViewSet
from .models import Team
from .serializers import TeamSerializer

# Create your views here.
class TeamViewSet(CustomModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
