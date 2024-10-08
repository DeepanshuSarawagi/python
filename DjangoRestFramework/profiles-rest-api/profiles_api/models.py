from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)  # This hashes the password instead of saving it as plain text in the DB
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create super user with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for the user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Return full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email

    class Meta:
        verbose_name_plural = "User Profiles"


class ProfileFeedItem(models.Model):
    """Profiles status updates"""
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateField(auto_now=True)

    def  __str__(self):
        """Return the model as a string"""
        return self.status_text
