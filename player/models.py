from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='player_images/', null=True, blank=True)
    bkash_transcation_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name