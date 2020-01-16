from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    icon = models.ImageField(
        upload_to='img/',
        verbose_name='アイコン',
        blank=True,
    )
    class Meta:
        verbose_name_plural = 'CustomUser'
