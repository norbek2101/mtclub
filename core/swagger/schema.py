from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.swagger.generator import BothHttpAndHttpsSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="MetSenat Club API",
        default_version="v1",
        description="MetSenat Club Uz",
        terms_of_service="https://www.club.metsenat.uz/policies/terms/",
        contact=openapi.Contact(email="info@metsenat.uz"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)
swagger_urlpatterns = [
    # re_path(
    #     r"^swagger(?P<format>\.json|\.yaml)$",
    #     schema_view.without_ui(cache_timeout=0),
    #     name="schema-json",
    # ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # re_path(
    #     r"^redoc/$",
    #     schema_view.with_ui("redoc", cache_timeout=0),
    #     name="schema-redoc",
    # ),
]
