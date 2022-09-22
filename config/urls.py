from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView

schema_view = get_schema_view(
    openapi.Info(
        title='Bai_Tushum',
        default_version='v1',
        description='TEST'
    ), public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('crm/', include('crm.urls')),
    path('',include('users.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),

]
