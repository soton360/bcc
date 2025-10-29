from django.db import models
from tournament.models import Tournament
from role.models import Role
from team.models import Team

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='player_images/', null=True, blank=True)
    bkash_transaction_id = models.CharField(max_length=50, null=True, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_players', null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
