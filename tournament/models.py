from django.db import models
from api.constants import CATEGORIES_CHOICES
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    registration_process = RichTextUploadingField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, default='cricket')
    is_active = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    registration_start = models.DateField()
    registration_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TournamentRuleTitle(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='tournament_rules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tournament.name} - {self.title}"


class TournamentRule(models.Model):
    rule_title = models.ForeignKey(TournamentRuleTitle, related_name='rules', on_delete=models.CASCADE)
    rule = models.TextField()

    def __str__(self):
        return f"Rule under {self.rule_title.title}"