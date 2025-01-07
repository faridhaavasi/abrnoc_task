from django.urls import path

from apps.authentication.v1.views.users import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
]