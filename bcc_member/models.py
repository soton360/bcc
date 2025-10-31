from django.db import models
from role.models import Role

# Create your models here.
class BCCMember(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='bcc_members/')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='bcc_member_roles')

    def __str__(self):
        return f"{self.name} - {self.category}"
    
