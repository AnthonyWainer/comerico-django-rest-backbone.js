from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.restaurants.urls')),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
