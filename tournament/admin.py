from django.contrib import admin
from .models import Tournament, TournamentRuleTitle, TournamentRule


class TournamentRuleInline(admin.TabularInline):
    model = TournamentRule
    extra = 1


class TournamentRuleTitleInline(admin.TabularInline):
    model = TournamentRuleTitle
    extra = 1


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'start_date', 'end_date')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)
    inlines = [TournamentRuleTitleInline]


@admin.register(TournamentRuleTitle)
class TournamentRuleTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tournament')
    inlines = [TournamentRuleInline]


@admin.register(TournamentRule)
class TournamentRuleAdmin(admin.ModelAdmin):
    list_display = ('rule_title', 'rule')
