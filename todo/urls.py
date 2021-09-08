import user_agents
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path

from rest_framework import routers
from rest_framework import permissions
from rest_framework.decorators import api_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from datetime import datetime
from todo.task.views import CategoryViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register("task-category", CategoryViewSet, basename="task-category")
router.register("task", TaskViewSet, basename="task")
now = datetime.now()

swagger_info = openapi.Info(
    title="SNI TODO Backend API",
    default_version="v1 (" + now.strftime("%Y/%m/%d %H:%M:%S") + ")",
    description="SNI TODO Backend API",
    contact=openapi.Contact(email="liliangjya@gmail.com"),
)

SchemaView = get_schema_view(
    public=True,
    permission_classes=[permissions.AllowAny],
)


@api_view(["GET"])
def plain_view(request):
    pass


def root_redirect(request):
    user_agent_string = request.META.get("HTTP_USER_AGENT", "")
    user_agent = user_agents.parse(user_agent_string)

    if user_agent.is_mobile:
        schema_view = "cschema-redoc"
    else:
        schema_view = "cschema-swagger-ui"

    return redirect(schema_view, permanent=True)


required_urlpatterns = [
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    # user djoser
    # path("auth/", include("djoser.urls.base")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
    # apps
    # path("", include("bsbackend.roles.urls")),
    # path("", include("bsbackend.cases.urls")),
    # swagger api
    path(
        "swagger-json",
        SchemaView.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", SchemaView.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "redoc-old/",
        SchemaView.with_ui("redoc-old", cache_timeout=0),
        name="schema-redoc-old",
    ),
    path("", root_redirect),
    # path("cases/", include("bsbackend.cases.urls")),
] + required_urlpatterns
