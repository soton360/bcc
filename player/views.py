from rest_framework import status
from rest_framework.response import Response

from api.views import CustomModelViewSet
from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
class PlayerViewSet(CustomModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer