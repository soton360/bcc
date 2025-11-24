from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer
from api.permissions import IsAdminOrCreateOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models


# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.filter(status="approved").all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAdminOrCreateOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['team', 'tournament']

    # def get_queryset(self):
    #     return Player.objects.filter(status="approved")

    @action(detail=False, methods=['get'], url_path='check-status')
    def check_status(self, request):
        phone = request.query_params.get('phone')
        bkash_id = request.query_params.get('bkash_transaction_id')
        tournament_id = request.query_params.get('tournament')

        if not tournament_id:
            raise ValueError("Please provide tournament_id")

        if not phone and not bkash_id:
            raise ValueError("Please provide phone or bkash_transaction_id")
            

        # Filter player by phone or bkash_transaction_id
        players = Player.objects.filter(
            tournament_id=tournament_id
        ).filter(
            models.Q(phone=phone) | models.Q(bkash_transaction_id=bkash_id)
        )

        serializer = self.get_serializer(players, many=True)
        return Response(serializer.data)



# /api/players/?team=3&tournament=1
# GET /api/players/check-status/?phone=01711111111
# GET /api/players/check-status/?bkash_transaction_id=TX123456


