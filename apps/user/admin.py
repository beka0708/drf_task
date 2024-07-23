from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "telegram_chat_id", "is_staff", "is_superuser")
    search_fields = ("username", "email", "telegram_chat_id")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email", "telegram_chat_id")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "telegram_chat_id",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
