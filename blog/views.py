from api.permissions import IsAdminOrReadOnly
from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-published_date')
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminOrReadOnly]