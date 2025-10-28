from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tournament.views import TournamentViewSet
from rules.views import RuleViewSet
from team.views import TeamViewSet
from role.views import RoleViewSet

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'rules', RuleViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'roles', RoleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


