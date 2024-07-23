from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    text = models.TextField(verbose_name="Текст")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author", blank=True
    )
    text = models.TextField(verbose_name="Текст комментария")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Mark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="marks")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="marks"
    )
    value = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Оценка"
    )

    def __str__(self):
        return f"{self.value} for {self.post}"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        unique_together = ("post", "user")
