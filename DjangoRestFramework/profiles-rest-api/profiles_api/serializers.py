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
                'style': {'input_type': 'password'}  # This setting ensures that password is hashed out when the user
                # types in the password input when invoking API
            }
        }

    # By default the Model Serializer allows user to create the simple objects in the DB. SO it user the default
    # create fn of the Object manager to create the objects. We want to override this functionality so that the
    # password created is hashed instead of a plain text.

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    # This method will ensure that when a user decides to update the password, it is saved as cleartext and we will be
    # unable to login. In order to override the default behaviour of DRF, we need to hash the user password when it is
    # updated
    def update(self, instance, validated_data):
        """ Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super(UserProfileSerializer, self).update(instance, validated_data)
