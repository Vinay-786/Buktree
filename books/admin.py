from django.contrib import admin
from .models import Chapter, Book

# class BookChapterAdmin(admin.ModelAdmin):
#     list_display = ('chapter_name', 'status')
#     actions = ['approve_books']

#     def approve_books(self, request, queryset):
#         queryset.update(status='APPROVED_BOOKS')
#     approve_books.short_description = "Approve selected books"


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chapter, AuthorAdmin)
admin.site.register(Book, AuthorAdmin)
