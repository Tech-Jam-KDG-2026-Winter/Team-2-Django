from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 他のモデルとの衝突を防ぐための設定を追加
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_set", # ここで別名を付ける
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permission_set", # ここで別名を付ける
        related_query_name="user",
    )