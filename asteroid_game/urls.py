# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

# Define the schema view for drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Asteroid Game API",
        default_version='v1',
        description="REST API to the Asteroid Game",
        terms_of_service="https://nathabee.de/terms-of-service/",
        contact=openapi.Contact(email="nathabe123@gmail.com"),
        license=openapi.License(name="BSD License", url="https://github.com/nathabee/django-asteroid/blob/main/LICENSE")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('game.urls')),
]

# Serve Swagger UI only in DEBUG mode
if settings.DEBUG:
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
        path('schema/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
else:
    # Serve custom HTML when not in DEBUG mode
    urlpatterns += [
        path('swagger/', TemplateView.as_view(template_name='swagger_unavailable.html'), name='swagger-unavailable'),
    ]

# The static file handling should be managed by your web server in production
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
