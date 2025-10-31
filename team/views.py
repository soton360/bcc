from .models import Team
from .serializers import TeamSerializer
from api.permissions import IsAdminOrReadOnly
from rest_framework import viewsets

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminOrReadOnly]
