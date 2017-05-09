from django.shortcuts import render
from .models import Article


def article_list(request):
    articles_list = Article.objects.all().filter(is_published=True)
    return render(request, 'newspaper/article_list.html', {'article_list': articles_list})
