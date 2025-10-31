from django.db import models
from tournament.models import Tournament


    
class Rule(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    rule = models.TextField()

    def __str__(self):
        return self.rule[:50]