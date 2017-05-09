from django.shortcuts import render
from .models import Article
# Create your views here.

def article_list(request):
    article_list = Article.objects.all().filter(is_published=True)
    return render(request, 'newspapper/article_list.html', {'article_list' : article_list})