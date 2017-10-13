from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^formularios/', include('formularios.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]