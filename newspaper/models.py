from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey('auth.User', related_name='articles')
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def publish(self):
        self.is_published = True
        self.save()


class Comment(models.Model):
    author = models.ForeignKey('auth.User', related_name='comments')
    article = models.ForeignKey('Article', related_name='comments')
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()


class Event(models.Model):
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
