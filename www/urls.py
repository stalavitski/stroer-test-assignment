from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from auth.views import ConvertTokenView

yasg_api_patterns = [
    re_path('auth/convert-token/?$', ConvertTokenView.as_view(), name='convert_token'),
    path('users/', include('users.urls', namespace='users')),
]

schema_view = get_schema_view(
    openapi.Info(
        title='',
        default_version='',
        description='',
        terms_of_service='',
    ),
    patterns=yasg_api_patterns,
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = yasg_api_patterns + [
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('admin/', admin.site.urls),
    # swagger drf-yasg
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
