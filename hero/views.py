from rest_framework import viewsets
from .models import HeroSection
from .serializers import HeroSectionSerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    permission_classes = [IsAdminOrReadOnly]