from django.db import models
import uuid

class Weather(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique identifier
    city_name = models.CharField(max_length=100)  # Name of the city
    country = models.CharField(max_length=50)  # Country code or name
    temperature = models.FloatField()
    description = models.CharField(max_length=255)  # Weather description (e.g., "clear sky")
    humidity = models.IntegerField()  # Humidity as a percentage
    wind_speed = models.FloatField()
    fetched_at = models.DateTimeField()  # Timestamp for data fetched from API
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation time
    updated_at = models.DateTimeField(auto_now=True)  # Last update time

    def __str__(self):
        return f"{self.city_name}, {self.country} - {self.description}"

    class Meta:
        verbose_name = "Weather"
        verbose_name_plural = "Weather Records"
        ordering = ['-fetched_at']  # Default sort: newest first
