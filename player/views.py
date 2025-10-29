from api.views import CustomModelViewSet
from .models import Player
from .serializers import PlayerSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class PlayerViewSet(CustomModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAdminOrReadOnly]