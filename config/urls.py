from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    path('dashboard/', include('src.dashboard.urls')),
    # User management
    path('accounts/', include('django.contrib.auth.urls')),
    # Local apps
    path('', include('src.users.urls')),
    path('', include('src.pages.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
