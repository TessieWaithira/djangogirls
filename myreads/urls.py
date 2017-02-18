from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.publish_read, name='publish_read'),
    url(r'^gist/(?P<pk>\d+)/$', views.gist_detail, name='gist_detail'),
    url(r'^gist/new/$', views.gist_new, name="gist_new"),
    url(r'^gist/(?P<pk>\d+)/edit/$', views.gist_edit, name='gist_edit'),
    url(r'^gist/drafts/$', views.gist_draft_list, name='gist_draft_list'),


]