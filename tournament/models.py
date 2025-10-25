from django.db import models

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    registration_start = models.DateField()
    registration_end = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name