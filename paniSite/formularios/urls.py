from django.conf.urls import url

from . import views


app_name = 'formularios'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id_grafico>[0-9]+)/$', views.grafico, name='grafico'),
]