from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_date")
    list_filter = ("created_date",)
    search_fields = ("text", "user__username")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "text", "created_date")
    list_filter = ("created_date", "user")
    search_fields = ("text", "user")
