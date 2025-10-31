
from .models import Rule
from .serializers import RuleSerializer
from api.permissions import IsAdminOrReadOnly
from rest_framework import viewsets


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAdminOrReadOnly]
