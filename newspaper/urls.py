from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
]
