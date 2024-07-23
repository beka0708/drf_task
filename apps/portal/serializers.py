from rest_framework import serializers
from .models import Post, Comment, Mark
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    average_mark = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "author", "text", "created_date", "average_mark"]

    def get_average_mark(self, obj):
        marks = obj.marks.all()
        if marks.exists():
            return sum(mark.value for mark in marks) / marks.count()
        return None


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "user", "text", "created_date"]

    def create(self, validated_data):
        request = self.context.get("request", None)
        if request and request.user.is_authenticated:
            validated_data["user"] = request.user.username
        return super().create(validated_data)


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ["id", "post", "user", "value"]
