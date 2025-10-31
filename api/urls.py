from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tournament.views import TournamentViewSet
from rules.views import RuleViewSet
from team.views import TeamViewSet
from role.views import RoleViewSet
from player.views import PlayerViewSet
from bcc_member.views import BCCMemberViewSet

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'rules', RuleViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'bcc-members', BCCMemberViewSet)



urlpatterns = [
    path('', include(router.urls)),
]


