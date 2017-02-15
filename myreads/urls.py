from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.publish_read, name='publish_read'),
]