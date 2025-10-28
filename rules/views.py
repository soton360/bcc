from rest_framework import status
from rest_framework.response import Response

from api.views import CustomModelViewSet
from .models import Rule
from .serializers import RuleSerializer


class RuleViewSet(CustomModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
