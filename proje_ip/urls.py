from django.conf.urls import include, url
from django.contrib import admin
from blogSitesi import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.gonderi_listesi, name='gonderi_listesi'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


