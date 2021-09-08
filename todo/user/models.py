from django.contrib.auth.models import AbstractUser
from djongo import models
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)

    # use email to login
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
