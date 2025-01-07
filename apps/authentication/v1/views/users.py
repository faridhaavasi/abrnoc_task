from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from apps.authentication.v1.serializers.users import UserSerializer

User = get_user_model()

class RegisterUserView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        """
        Register a new user
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            if User.objects.filter(email=email).exists():
                return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()

            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
