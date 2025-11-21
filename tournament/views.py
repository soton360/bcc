from rest_framework import viewsets
from .models import Tournament, TournamentRuleTitle, TournamentRule
from .serializers import TournamentSerializer, TournamentRuleTitleSerializer, TournamentRuleSerializer
from api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all().order_by('-created_at')
    serializer_class = TournamentSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active']


class TournamentRuleTitleViewSet(viewsets.ModelViewSet):
    queryset = TournamentRuleTitle.objects.all()
    serializer_class = TournamentRuleTitleSerializer


class TournamentRuleViewSet(viewsets.ModelViewSet):
    queryset = TournamentRule.objects.all()
    serializer_class = TournamentRuleSerializer

