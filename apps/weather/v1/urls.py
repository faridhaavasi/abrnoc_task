from django.urls import path, include

from apps.weather.v1.views.weather_views import  WeatherCreateView
from apps.weather.v1.views.weather_views import  WeatherViewSet
from rest_framework.routers import DefaultRouter

rotuer = DefaultRouter()                                       
rotuer.register('weather', WeatherViewSet, basename='weather')  # Register the viewset with the router         



urlpatterns = [
    path('weather/create/', WeatherCreateView.as_view(), name='weather-create'),  # Create a new record
    path('', include(rotuer.urls)),

]