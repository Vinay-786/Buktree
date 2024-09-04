from django.contrib import admin
from .models import Chapter, Book, Feedback


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'verified')
    search_fields = ['title']

    def toggle_verified_status(self, request, queryset):
        queryset.update(verified=fields('verified').bitwise_xor(True))
        self.message_user(
            request, f"Successfully toggled verified status for {queryset.count()} books.")

    # Register the action
    toggle_verified_status.short_description = "Toggle Verified status for selected books"
    actions = [toggle_verified_status]


admin.site.register(Book, BookAdmin)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'content')
    search_fields = ['name']


admin.site.register(Chapter, ChapterAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']


admin.site.register(Feedback, FeedbackAdmin)
