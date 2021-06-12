from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import uuid


class Manager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, first_name, last_name, password, **extra_fields)


class User(AbstractUser):
    DEFAULT_AVATAR_URL = 'https://res.cloudinary.com/ddl2pf4qh/image/upload/v1623512852/24-248253_user-profile-default-image-png-clipart-png-download_qwj0qi.png'
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    avatar_url = models.URLField(default=DEFAULT_AVATAR_URL)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = Manager()

    def __str__(self):
        return self.email



