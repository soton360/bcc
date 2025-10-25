from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tournament.views import TournamentViewSet

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


