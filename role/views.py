from rest_framework import status
from rest_framework.response import Response

from api.views import CustomModelViewSet
from .models import Role
from .serializers import RoleSerializer

# Create your views here.
class RoleViewSet(CustomModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
