from django.conf import settings
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Post, Comment
from .permissions import IsOwnerOrStaffOrReadOnly
from .serializers import PostSerializer, CommentSerializer, MarkSerializer
import telebot

User = get_user_model()
bot_token = settings.TELEGRAM_BOT_TOKEN
bot = telebot.TeleBot(bot_token)


def send_telegram_message(chat_id, message):
    bot.send_message(chat_id, message)


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        chat_id = self.request.user.telegram_chat_id
        if chat_id:
            send_telegram_message(chat_id, "Ваш пост успешно опубликован!")


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["post_id"])

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs["post_id"],
            user=(
                self.request.user.username
                if self.request.user.is_authenticated
                else serializer.validated_data["user"]
            ),
        )


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["post_id"])


class MarkCreateView(generics.CreateAPIView):
    serializer_class = MarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs["post_id"])
        serializer.save(post=post, user=self.request.user)
