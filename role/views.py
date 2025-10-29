from api.views import CustomModelViewSet
from .models import Role
from .serializers import RoleSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class RoleViewSet(CustomModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminOrReadOnly]
