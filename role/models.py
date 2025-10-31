from django.db import models
from api.constants import CATEGORIES_CHOICES

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, default='cricket')

    def __str__(self):
        return self.name
