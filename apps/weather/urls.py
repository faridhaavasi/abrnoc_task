from django.urls import path, include

app_name = 'weather'
urlpatterns = [
    path('weather/api/v1/', include('apps.weather.v1.urls'), name='weather'),
]