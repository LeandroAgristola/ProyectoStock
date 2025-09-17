from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    
    # Redireccionar la URL raíz ('/') a la página de login de management
    path('', RedirectView.as_view(url='management/login/', permanent=True)),
    path('admin/', admin.site.urls),
    path('management/', include('management.urls')),
    path('products/', include('products.urls')),
    path('staff/', include('staff.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)