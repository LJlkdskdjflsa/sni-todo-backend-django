from rest_framework import serializers

from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    """
    serialize category objects

    Args:
        serializers ([type]): [description]
    """

    class Meta:
        model = Category
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    """
    serialize task objects

    Args:
        serializers ([type]): [description]
    """

    class Meta:
        model = Task
        fields = "__all__"
