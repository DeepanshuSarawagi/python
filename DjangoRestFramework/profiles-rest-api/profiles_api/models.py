from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for the user in the system"""
    email = models.EmailField(max_length=255, unique=True)
