from django.urls import path
from .views import (
    PostListCreateView,
    PostCreateView,
    PostDetailView,
    CommentListCreateView,
    CommentDetailView,
    MarkCreateView,
)

urlpatterns = [
    path("post/", PostListCreateView.as_view(), name="post_list"),
    path("post_add/", PostCreateView.as_view(), name="post_add"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path(
        "post/<int:post_id>/comment/",
        CommentListCreateView.as_view(),
        name="comment_list",
    ),
    path(
        "post/<int:post_id>/comment_add/",
        CommentListCreateView.as_view(),
        name="comment_add",
    ),
    path(
        "post/<int:post_id>/comment/<int:pk>/",
        CommentDetailView.as_view(),
        name="comment_detail",
    ),
    path("post/<int:post_id>/mark_add/", MarkCreateView.as_view(), name="mark_add"),
]
