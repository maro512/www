from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views


def article_list(request):
    articles_list = Article.objects.filter(is_published=True).order_by('-date')
    return render(request, 'newspaper/article_list.html', {'article_list': articles_list})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=pk).order_by('-date')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()
        return render(request, 'newspaper/article_detail.html', {'article': article, 'comments': comments, 'form': form})


@login_required
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'newspaper/article_edit.html', {'form': form})


@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'newspaper/article_edit.html', {'form': form})


@login_required
def not_published_list(request):
    articles_list = Article.objects.filter(is_published=False).order_by('-date')
    return render(request, 'newspaper/article_list.html', {'article_list': articles_list})


@login_required
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('article_detail', pk=pk)


@login_required
def article_remove(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')


@login_required
def comment_remove(request, fk, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('article_detail', pk=fk)


def user_new(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(views.login)
    else:
        form = CreateUserForm()
    return render(request, 'registration/register.html', {'form': form})

