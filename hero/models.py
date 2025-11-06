from django.db import models

# Create your models here.
class HeroSection(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    def __str__(self):
        return self.title
    

