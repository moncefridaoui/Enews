
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from newsApp.views import News

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('news/',include('newsApp.urls')),
    path('news/', News, name='news'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
