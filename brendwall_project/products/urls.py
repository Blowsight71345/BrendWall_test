from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import ProductListCreateAPIView, index

schema_view = get_schema_view(
    openapi.Info(
        title="BrendWall API",
        default_version='v1',
        description="BrendWall test API",
    ),
    public=True
)

urlpatterns = [
    path('', index, name='index'),
    path('products/', ProductListCreateAPIView.as_view(),
         name='products-list-create'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
