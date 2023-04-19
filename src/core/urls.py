from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from api.v1 import urls as api_url
from core import settings
from core.yasg import urlpatterns2

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(api_url)),
    path('silk/', include('silk.urls', namespace='silk')),
]
urlpatterns += urlpatterns2

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
