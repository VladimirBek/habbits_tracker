from rest_framework import generics
from users.models import User
from users.serializers import UserListSerializer, UserCreateSerializer


class UserListView(generics.ListAPIView):
    """Controller for displaying a list of all users"""

    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserCreateView(generics.CreateAPIView):
    """Controller for creating an instance of the model 'User'"""

    serializer_class = UserCreateSerializer