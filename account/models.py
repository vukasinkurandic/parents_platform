from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'family'),
        (2, 'babysitter'),
    )
    USER_MEMBERSHIP = (
        (1, 'FREE'),
        (2, 'SILVER'),
        (3, 'GOLD'),
    )
    username = None
    email = models.EmailField(('email address'), unique=True)
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default=1)
    auth_token = models.CharField(max_length=100)
    membership = models.PositiveSmallIntegerField(
        choices=USER_MEMBERSHIP, default=1)
    is_email_verified = models.BooleanField(default=False)
    is_terms_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

# ready for user pass test email_verified_check

# def email_verified_check(user):
#     return user.is_email_verified

# from account . models import email_verified_check
# from django.contrib.auth.decorators import login_required, user_passes_test

# @user_passes_test(email_verified_check, login_url='account:login', redirect_field_name=None)
