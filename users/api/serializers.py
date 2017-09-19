from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'is_staff')


class UserTokenSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Only returns the user token
    """
    auth_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('auth_token',)
