from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^article/new/$', views.article_new, name='article_new'),
    url(r'^article/(?P<pk>[0-9]+)/edit/$', views.article_edit, name='article_edit'),
    url(r'^article/(?P<pk>[0-9]+)/new_comment/$', views.comment_new, name='comment_new'),
]
