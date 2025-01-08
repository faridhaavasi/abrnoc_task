from rest_framework import serializers
from apps.weather.models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'  # Include all fields from the model
        read_only_fields = ('id', 'created_at', 'updated_at', 'fetched_at')  # Prevent editing these fields


class WeatherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['city_name', 'country']  # Include only these fields
    