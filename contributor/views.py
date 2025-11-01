from rest_framework import viewsets
from .models import Contributor
from .serializers import ContributorSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAdminOrReadOnly]