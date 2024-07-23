from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_chat_id = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Email")
    is_staff = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk and self.is_superuser:
            self.is_staff = True
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
