"""Сериализаторы для приложения api."""
from rest_framework import serializers

from posts.models import Comment, Post


class BaseSerializer(serializers.ModelSerializer):
    """Сериализатор c общими атрибутами моделей."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )


class PostSerializer(BaseSerializer):
    """Сериализатор для модели Post."""

    class Meta:
        """Мета-класс сериализатора модели Post."""

        fields = '__all__'
        model = Post


class CommentSerializer(BaseSerializer):
    """Сериализатор для модели Comment."""

    class Meta:
        """Мета-класс сериализатора модели Comment."""

        fields = '__all__'
        model = Comment
