from django.contrib import admin
from .models import Weather

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('city_name', 'country', 'temperature', 'description', 'humidity', 'wind_speed', 'fetched_at')
    
    # Fields to filter the list by
    list_filter = ('country', 'fetched_at')
    
    # Fields to enable search functionality
    search_fields = ('city_name', 'country')
    
    # Ordering of the records in the admin panel
    ordering = ['-fetched_at']
    
    # Fields to display in the detail view (optional)
    readonly_fields = ('created_at', 'updated_at', 'fetched_at')
