from django.db import models
from django.utils import timezone


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User');
    data = models.DateField(default=timezone.now());
    title = models.CharField(max_length=200);
    content = models.TextField();
    is_published = models.BooleanField();

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    article = models.ForeignKey('Article')
    date = models.DateTimeField(default=timezone.now())
    content = models.TextField()









