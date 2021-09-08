from django.urls import include, path
from rest_framework import routers

from todo.task.views import CategoryViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register("task-category", CategoryViewSet, basename="task-category")
router.register("task", TaskViewSet, basename="task")
