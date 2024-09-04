from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView
from asteroid_game.views import custom_404  # Import your custom 404 view
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


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
    #path('static/html/<path:path>', TemplateView.as_view(template_name='html/index.html'), name='html'),
    #path('', TemplateView.as_view(template_name='html/index.html'), name='index'),  # Serve static/html/index.html
    
    
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

# Serve static files only in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Redirect all unknown routes to static/html/index.html
urlpatterns += [
    re_path(r'^.*$', RedirectView.as_view(url='/static/html/index.html', permanent=False), name='index')
]

# Custom error handlers
handler404 = custom_404
