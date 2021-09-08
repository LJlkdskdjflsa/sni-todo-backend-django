from datetime import datetime, timedelta
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from djongo import models
from djongo.storage import GridFSStorage
from todo.utils.models import TrackingBaseModel


class Category(TrackingBaseModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "task catogory"
        verbose_name_plural = "task catogories"

    def __str__(self):
        return str(self.title)


class Task(TrackingBaseModel):
    """
    task

    Returns:
        [type]: [description]
    """

    # task info
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    priority = models.IntegerField(null=True, blank=True)
    estimated_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "task"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.title)
