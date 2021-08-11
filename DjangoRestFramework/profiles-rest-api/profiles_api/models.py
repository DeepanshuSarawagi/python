from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for the user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
