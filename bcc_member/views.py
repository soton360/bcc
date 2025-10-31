from rest_framework import viewsets
from .models import BCCMember
from .serializers import BCCMemberSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class BCCMemberViewSet(viewsets.ModelViewSet):
    queryset = BCCMember.objects.all()
    serializer_class = BCCMemberSerializer
    permission_classes = [IsAdminOrReadOnly]
