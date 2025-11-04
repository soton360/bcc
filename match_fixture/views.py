from rest_framework import viewsets
from .models import MatchFixture
from .serializers import MatchFixtureSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class MatchFixtureViewSet(viewsets.ModelViewSet):
    queryset = MatchFixture.objects.all().order_by('-match_date_time')
    serializer_class = MatchFixtureSerializer
    permission_classes = [IsAdminOrReadOnly]