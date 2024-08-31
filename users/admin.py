from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class Profile(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_img')}),
    )


admin.site.register(User, Profile)

