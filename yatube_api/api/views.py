"""Вьюсеты для приложения api."""
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

from posts.models import Follow, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


class BaseViewSet(viewsets.ModelViewSet):
    """Общий вьюсет с повторяющимися настройками."""

    permission_classes = (IsAuthorOrReadOnly,)


class PostViewSet(BaseViewSet):
    """Вьюсет для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Устанавливает автора поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class CommentViewSet(BaseViewSet):
    """Вьюсет для модели Comment."""

    serializer_class = CommentSerializer

    def __get_post(self):
        """Приватный метод получения одного поста."""
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Возвращает комментарии для конкретного поста."""
        return self.__get_post().comments.all()

    def perform_create(self, serializer):
        """Создаёт комментарий для конкретного поста."""
        serializer.save(author=self.request.user, post=self.__get_post())


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Follow."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Только подписки текущего пользователя."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Подписка от текущего пользователя."""
        serializer.save(user=self.request.user)
