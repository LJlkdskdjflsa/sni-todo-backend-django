from todo.utils import viewsets
from .serializers import CategorySerializer, TaskSerializer
from .models import Category, Task
from rest_framework import filters


class CategoryViewSet(viewsets.ModelViewSet):
    """案件類型視圖集

    Args:
        viewsets ([type]): [description]
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    view of task
        Args:
            viewsets ([type]): [description]
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ["title", "description"]
    search_fields = ["title", "description"]
