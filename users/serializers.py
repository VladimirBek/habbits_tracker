from rest_framework import serializers
from users.models import User


class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer for model User.
    Use with invoke GET requests in CustomUserListView
     """

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for model User.
    Use with invoke POST requests in CustomUserCreateView
    """

    class Meta:
        model = User
        fields = ('password', 'email', 'tg_username',)

    def create(self, validated_data):
        """
        :param validated_data: Data, provided by the client.
        :return: New instance of the model User.
        """

        new_custom_user = User.objects.create_user(**validated_data)
        return new_custom_user
