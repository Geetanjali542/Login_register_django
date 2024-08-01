from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin

from . import views

# from dummy import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('dummy/', include('dummy.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

