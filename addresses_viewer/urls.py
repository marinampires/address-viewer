
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^addresses$', views.addresses, name='addresses'),
    url(r'^api/', include('addresses_viewer.api.urls')),
    
]
