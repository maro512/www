from django.shortcuts import render, get_object_or_404
from .models import Article
from .models import Comment


def article_list(request):
    articles_list = Article.objects.filter(is_published=True).order_by('date')
    return render(request, 'newspaper/article_list.html', {'article_list': articles_list})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=pk).order_by('date')
    return render(request, 'newspaper/article_detail.html', {'article': article, 'comments': comments})
