from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^article/new/$', views.article_new, name='article_new'),
    url(r'^article/(?P<pk>[0-9]+)/edit/$', views.article_edit, name='article_edit'),
    url(r'^drafts/$', views.not_published_list, name='not_published_list'),
    url(r'^article/(?P<pk>[0-9]+)/publish/$', views.article_publish, name='article_publish'),
    url(r'^article/(?P<pk>[0-9]+)/remove/$', views.article_remove, name='article_remove'),
    url(r'^article/(?P<fk>[0-9]+)/comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]
