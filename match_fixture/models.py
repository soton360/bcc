from django.db import models
from tournament.models import Tournament
# Create your models here.
class MatchFixture(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    match_date_time = models.DateTimeField()
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    result = models.CharField(max_length=255, null=True, blank=True)
    team_a_score = models.CharField(max_length=100, null=True, blank=True)
    team_b_score = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.team_a} vs {self.team_b} on {self.title}"
    

