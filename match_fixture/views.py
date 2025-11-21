from rest_framework import viewsets
from .models import MatchFixture
from .serializers import MatchFixtureSerializer, MatchFixtureFilter
from api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class MatchFixtureViewSet(viewsets.ModelViewSet):
    queryset = MatchFixture.objects.all().order_by('-match_date_time')
    serializer_class = MatchFixtureSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MatchFixtureFilter