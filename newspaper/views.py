from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Article, Comment, Favorite
from .forms import ArticleForm, CommentForm, CreateUserForm, FavoriteForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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
    return render(request, 'newspaper/article_detail.html',
                  {'article': article, 'comments': comments, 'form': form} )


def article_new(request):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
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


def article_edit(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
    article = get_object_or_404(Article, pk=pk)
    if not request.user.is_staff and not request.user == article.author:
        return render(request, 'errors/403.html', status=403)
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


def not_published_list(request):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
    if not request.user.is_staff:
        return render(request, 'errors/403.html', status=403)
    articles_list = Article.objects.filter(is_published=False).order_by('-date')
    return render(request, 'newspaper/not_published_list.html', {'article_list': articles_list})


def article_publish(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
    if not request.user.is_staff:
        return render(request, 'errors/403.html', status=403)
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('article_detail', pk=pk)


def article_remove(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
    article = get_object_or_404(Article, pk=pk)
    if not request.user.is_staff and not request.user == article.author:
        return render(request, 'errors/403.html', status=403)
    article.delete()
    return redirect('article_list')


def comment_remove(request, fk, pk):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
    comment = get_object_or_404(Comment, pk=pk)
    if not request.user.is_staff and not request.user == comment.author:
        return render(request, 'errors/403.html', status=403)
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


def my_article(request):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
    articles_list = Article.objects.filter(author=request.user).order_by('-date')
    return render(request, 'newspaper/my_article.html', {'article_list': articles_list})


def user_list(request):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
    if not request.user.is_staff:
        return render(request, 'errors/403.html', status=403)
    users = User.objects.all()
    return render(request, 'newspaper/user_list.html', {'users': users})

@login_required
def favorite_add(request, pk):  # post
    article = get_object_or_404(Article, pk=pk)
    favorite = Favorite.objects.all().filter(user=request.user, article=article)
    if bool(favorite) is False:
        favorite = Favorite()
        favorite.user = request.user
        favorite.article = article
        favorite.save()
    return redirect('article_detail', pk=article.pk)


@login_required
def favorite_remove(request, pk):  # post
    favorite = get_object_or_404(Favorite, pk=pk)
    favorite.delete()
    return redirect('favorite_list')


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'newspaper/favorite_list.html', {'favorites': favorites})


def favorite_edit(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'errors/401.html', status=401)
    favorite = get_object_or_404(Favorite, pk=pk)
    if not request.user.is_staff and not request.user == favorite.user:
        return render(request, 'errors/403.html', status=403)
    if request.method == "POST":
        form = FavoriteForm(request.POST)
        if form.is_valid():
            favorite.comment = form.cleaned_data['comment']
            favorite.rating = form.cleaned_data['rating']
            favorite.save()
            return redirect('favorite_list')
    else:
        form = FavoriteForm()
    return render(request, 'newspaper/favorite_edit.html', {'form': form})