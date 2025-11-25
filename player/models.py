from django.db import models
from tournament.models import Tournament
from role.models import Role
from team.models import Team

# Create your models here.
class Player(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='player_images/', null=True, blank=True)
    bkash_transaction_id = models.CharField(max_length=50, null=True, blank=True, unique=True, db_index=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_players', null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
    
