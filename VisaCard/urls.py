"""
URL configuration for VisaCard project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cards.urls')),
]
if settings.STATIC_ROOT:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
