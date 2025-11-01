from django.db import models

# Create your models here.
class PowerHouse(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='power_house/')

    def __str__(self):
        return self.name