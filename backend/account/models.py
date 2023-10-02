from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from account.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    id = models.IntegerField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.email