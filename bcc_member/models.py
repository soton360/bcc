from django.db import models
from api.constants import CATEGORIES_CHOICES
from role.models import Role

# Create your models here.
class BCCMember(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='bcc_members/')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.role.name if self.role else 'No Role'}"
    
