from django.conf.urls import url
from addresses_viewer.api import views

urlpatterns = [
    url(r'^addresses/$', views.addresses_list),
]