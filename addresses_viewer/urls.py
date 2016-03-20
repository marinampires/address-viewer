
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^viewport$', views.viewport, name='viewport'),
    url(r'^get_table_id$', views.get_table_id, name='get_table_id'),
    url(r'^get_addresses$', views.get_addresses, name='get_addresses'),
    url(r'^', include('addresses_viewer.api.urls')),
    
]
