from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        rid_only_fields = ('id', )
        is_required = ('username', 'email', 'first_name', 'last_name')
        