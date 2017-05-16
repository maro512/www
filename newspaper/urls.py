from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^article/new/$', views.article_new, name='article_new'),
    url(r'^article/(?P<pk>[0-9]+)/edit/$', views.article_edit, name='article_edit'),
    url(r'^drafts/$', views.not_published_list, name='not_published_list'),
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^events/$', views.event_list, name='event_list'),
    url(r'^event/new/$', views.event_new, name='event_new'),
    url(r'^event/(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>[0-9]+)/remove/$', views.event_remove, name='event_remove'),
    url(r'^my_article/$', views.my_article, name='my_article'),
    url(r'^article/(?P<pk>[0-9]+)/publish/$', views.article_publish, name='article_publish'),
    url(r'^article/(?P<pk>[0-9]+)/remove/$', views.article_remove, name='article_remove'),
    url(r'^article/(?P<fk>[0-9]+)/comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^accounts/register/$', views.user_new, name='user_new'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
