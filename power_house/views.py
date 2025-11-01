from rest_framework import viewsets
from .models import PowerHouse
from .serializers import PowerHouseSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class PowerHouseViewSet(viewsets.ModelViewSet):
    queryset = PowerHouse.objects.all()
    serializer_class = PowerHouseSerializer
    permission_classes = [IsAdminOrReadOnly]
