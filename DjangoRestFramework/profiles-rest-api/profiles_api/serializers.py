from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API view"""
    name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,  # Setting this to True ensures we can only create new objects but not
                # retrieve/update the existing objects
                'style': {'input_type': 'password'}
            }
        }