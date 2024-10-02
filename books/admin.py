from django.contrib import admin
from .models import Chapter, Book, Feedback


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'verified')
    search_fields = ['title']


admin.site.register(Book, BookAdmin)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'content')
    search_fields = ['name', 'book__title']
    list_filter = ['book']
    ordering = ('book', 'name')


admin.site.register(Chapter, ChapterAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']


admin.site.register(Feedback, FeedbackAdmin)
