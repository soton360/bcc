from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tournament.views import TournamentViewSet
from rules.views import RuleViewSet

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'rules', RuleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


