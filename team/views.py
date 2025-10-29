from api.views import CustomModelViewSet
from .models import Team
from .serializers import TeamSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class TeamViewSet(CustomModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminOrReadOnly]
