from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tournament.views import TournamentViewSet
from team.views import TeamViewSet
from role.views import RoleViewSet
from player.views import PlayerViewSet
from bcc_member.views import BCCMemberViewSet
from gallery.views import GalleryViewSet
from sponsor.views import SponsorViewSet
from power_house.views import PowerHouseViewSet

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'bcc-members', BCCMemberViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'power-houses', PowerHouseViewSet)



urlpatterns = [
    path('', include(router.urls)),
]


