from django.db import models
from role.models import Role

# Create your models here.
class BCCMember(models.Model):
    CATEGORIES_CHOICES = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('badminton', 'Badminton'),
    ]

    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORIES_CHOICES, default='cricket')
    image = models.ImageField(upload_to='bcc-members/')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='bcc_member_roles')

    def __str__(self):
        return f"{self.name} - {self.category}"
    
