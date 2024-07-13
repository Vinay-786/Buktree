# from django.db import models

# # Create your models here.


# class chapters(models.Model):
#     chapters_id=models.AutoField(primary_key=True)
#     verified=models.BooleanField(default=True)
#     content=models.TextField()
#     chapter_name=models.TextField()


# class books(models.Model):
#     book_id= models.AutoField(primary_key=True)
#     book_name = models.CharField(max_length=255)
#     book_description = models.TextField(max_length=250)
#     chapter_number = models.IntegerField()
#     cover= models.ImageField(default='default.jpg', upload_to='book_images')
#     author=models.CharField(max_length=50)
#     chapters=models.ForeignKey(chapters, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(
        Book, related_name='chapters', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.book.title} - Chapter {self.order}: {self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
