from django.db import models

# Create your models here.
class TournamentRule(models.Model):
    tournament_title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.tournament_title
    
class Rules(models.Model):
    tournament_rule = models.ForeignKey(TournamentRule, on_delete=models.CASCADE)
    rule = models.TextField()

    def __str__(self):
        return self.rule