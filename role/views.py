from .models import Role
from .serializers import RoleSerializer
from api.permissions import IsAdminOrReadOnly
from rest_framework import viewsets

# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminOrReadOnly]
