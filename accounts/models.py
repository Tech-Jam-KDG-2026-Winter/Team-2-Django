from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name="custom_user_set",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name="custom_user_permission_set",
    )