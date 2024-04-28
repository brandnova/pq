from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from home.views import index

urlpatterns = [
    path('', index, name='index'),
    path('home/', include('home.urls')),
    path('docs/', include('docs.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
