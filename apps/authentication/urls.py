from django.urls import path, include

apps_name = 'authentication'
urlpatterns = [
    path('api/v1/', include('apps.authentication.v1.urls')),
]
