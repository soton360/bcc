from django.db import models
from api.constants import CATEGORIES_CHOICES

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, default='cricket')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
