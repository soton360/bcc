from api.views import CustomModelViewSet
from .models import Player
from .serializers import PlayerSerializer
from api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class PlayerViewSet(CustomModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['team', 'tournament']


# /api/players/?team=3
# /api/players/?tournament=2
# /api/players/?team=3&tournament=1

