from django.db import models
from django.conf import settings
from django.utils import timezone
from django_quill.fields import QuillField


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)
    book_cover = models.ImageField(
        upload_to="book_cover", default='/default/default_book.jpg')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="books",
        on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now, blank=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(
        Book, related_name='chapters', on_delete=models.CASCADE)
    content = QuillField()
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}: {self.name}"


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=250)

    def __str__(self):
        return f"Message: {self.message}"
