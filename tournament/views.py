from rest_framework import viewsets
from .models import Tournament, TournamentRuleTitle, TournamentRule
from .serializers import TournamentSerializer, TournamentRuleTitleSerializer, TournamentRuleSerializer
from api.permissions import IsAdminOrReadOnly


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all().order_by('-created_at')
    serializer_class = TournamentSerializer
    permission_classes = [IsAdminOrReadOnly]


class TournamentRuleTitleViewSet(viewsets.ModelViewSet):
    queryset = TournamentRuleTitle.objects.all()
    serializer_class = TournamentRuleTitleSerializer


class TournamentRuleViewSet(viewsets.ModelViewSet):
    queryset = TournamentRule.objects.all()
    serializer_class = TournamentRuleSerializer

