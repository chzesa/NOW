from django.urls import path
from django.urls.conf import include
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer

from . import views
from .routers import Router, ApiRouter

# Set root renderers in constructor
router = Router()
router.register(r'museums', views.MuseumWebViewSet)
router.register(r'localities', views.LocalityWebViewSet)

apirouter = ApiRouter()
apirouter.register(r'museums', views.MuseumViewSet, 'api-museums')
apirouter.register(r'localities', views.LocalityViewSet, 'api-localities')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(apirouter.urls)),
    path('api/', get_schema_view(
        title="NOW - New and Old Worlds",
        description="NOW database API Schema",
        version="1.0.0",
        renderer_classes=[JSONOpenAPIRenderer],
        patterns=apirouter.urls,
    ), name='openapi-schema'),
    path('auth/', include('rest_framework.urls')),
]
