from django.contrib import admin
from .models import Player

# Register your models here.
# admin.site.register(Player)
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'team')
    list_filter = ('team',)
    search_fields = ('name', 'phone')

