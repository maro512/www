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
    url(r'^favorite/$', views.favorite_list, name='favorite_list'),
    #url(r'^favorite/new/$', views.favorite_add, name='favorite_add'),
    url(r'^favorite/(?P<pk>[0-9]+)/edit/$', views.favorite_edit, name='favorite_edit'),
    url(r'^favorite/(?P<pk>[0-9]+)/remove/$', views.favorite_remove, name='favorite_remove'),
    url(r'^my_article/$', views.my_article, name='my_article'),
    url(r'^article/(?P<pk>[0-9]+)/publish/$', views.article_publish, name='article_publish'),
    url(r'^article/(?P<pk>[0-9]+)/remove/$', views.article_remove, name='article_remove'),
    url(r'^article/(?P<fk>[0-9]+)/comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^accounts/register/$', views.user_new, name='user_new'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
