from rest_framework import viewsets
from .models import Gallery
from .serializers import GallerySerializer
from api.permissions import IsAdminOrReadOnly

# Create your views here.
class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAdminOrReadOnly]
