from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.publish_read, name='publish_read'),
    url(r'^gist/(?P<pk>\d+)/$', views.gist_detail, name='gist_detail'),
    url(r'^gist/new/$', views.gist_new, name="gist_new"),
    url(r'^gist/(?P<pk>\d+)/edit/$', views.gist_edit, name='gist_edit'),
    url(r'^gist/drafts/$', views.gist_draft_list, name='gist_draft_list'),
    url(r'^gist(?P<pk>\d+)/publish/$', views.gist_publish, name='gist_publish'),
    url(r'^gist/(?P<pk>\d+)/delete/$', views.gist_delete, name='gist_delete'),
    url(r'^gist/(?P<pk>\d+)/comment/$', views.add_comment_to_gist, name='add_comment_to_gist'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),


]