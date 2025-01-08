from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated  # Import the permission class
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests
from apps.weather.models import Weather
from apps.weather.v1.serializers.weather_serializer import WeatherSerializer, WeatherCreateSerializer
from datetime import datetime
import json



class WeatherCreateView(GenericAPIView):
    """
    Create a new weather record by fetching data from OpenWeatherMap API (Only for authenticated users).
    """
    serializer_class = WeatherCreateSerializer
    permission_classes = [IsAuthenticated]  # Require login

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            city_name = serializer.validated_data.get('city_name') 
            country = serializer.validated_data.get('country')
            if not city_name or not country:
                return Response({'error': 'City name and country are required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Fetch weather data from OpenWeatherMap API
            # api_key = '051f31d206f22ed317258ddff7c91bf5'
            api_key = settings.OPENWEATHERMAP_API_KEY

            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country}&appid={api_key}&units=metric"
            response = requests.get(url)  # Use GET instead of POST
            if response.status_code != 200:
                return Response({'error': 'Failed to fetch data from OpenWeatherMap.', 'api_key': api_key}, status=response.status_code)
            
            data = response.json()
            print(data)
            weather_data = {
                'city_name': city_name,
                'country': country,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'fetched_at': datetime.now(),
            }

            # Serialize and save the data
            Weather.objects.create(**weather_data)
            return Response({'message': 'Weather data saved successfully and save in database', 'data': response}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class WeatherViewSet(ModelViewSet):
    """
    A ViewSet for handling retrieve, update, and delete operations for Weather records.
    """
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthenticated]  # Require login

    def create(self, request, *args, **kwargs):
        """
        Disable the POST method in the ViewSet.
        """
        return Response({'detail': 'POST method is not allowed for this endpoint.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_queryset(self):
        """
        Optionally filter the weather records by city or country from query parameters.
        """
        queryset = super().get_queryset()
        city_name = self.request.query_params.get('city_name')
        country = self.request.query_params.get('country')
        if city_name:
            queryset = queryset.filter(city_name__icontains=city_name)
        if country:
            queryset = queryset.filter(country__icontains=country)
        return queryset