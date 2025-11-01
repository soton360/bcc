from rest_framework import viewsets
from .models import Sponsor
from .serializers import SponsorSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [IsAdminOrReadOnly]