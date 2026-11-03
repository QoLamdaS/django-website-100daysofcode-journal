from django.contrib import admin
from .models import DayLog

@admin.register(DayLog)
class DayLogAdmin(admin.ModelAdmin):
    list_display = ('day_number', 'title', 'date')
    search_fields = ('title', 'description')
    list_filter = ('date',)