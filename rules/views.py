
from api.views import CustomModelViewSet
from .models import Rule
from .serializers import RuleSerializer
from api.permissions import IsAdminOrReadOnly


class RuleViewSet(CustomModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAdminOrReadOnly]
