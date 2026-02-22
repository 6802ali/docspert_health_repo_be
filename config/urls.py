from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from patient.views import PatientViewSet
from consultation.views import ConsultationViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'consultations', ConsultationViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Docspert Health API",
        default_version='v1',
        description="API documentation for Docspert Health Task",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include("user.urls")),
    # Swagger
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]