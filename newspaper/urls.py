from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
]
