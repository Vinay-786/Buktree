from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    book_cover = models.ImageField(upload_to="media", default='default.jpg')
    author = models.ForeignKey(
        User, related_name="books", on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(
        Book, related_name='chapters', on_delete=models.CASCADE)
    content = models.TextField()
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.book.title} - Chapter {self.order}: {self.name}"
