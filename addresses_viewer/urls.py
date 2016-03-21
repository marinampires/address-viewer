
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^get_addresses$', views.get_addresses, name='get_addresses'),
    url(r'^', include('addresses_viewer.api.urls')),
    
]
