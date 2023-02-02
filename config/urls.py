from django.contrib import admin
from django.urls import path, include,re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from . import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Bai_Tushum',
        default_version='v1',
        description='TEST'
    ), public=True
)

urlpatterns = [
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('crm/', include('crm.urls')),
    path('', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
