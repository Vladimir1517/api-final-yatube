"""Сериализаторы для приложения api."""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


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
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        """Мета-класс сериализатора модели Group."""

        model = Group
        fields = '__all__'
        read_only_fields = ('slug',)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        """Мета-класс сериализатора модели Follow."""

        model = Follow
        fields = '__all__'
        read_only_fields = ('user',)

    def validate_following(self, value):
        """Проверяем, что пользователь не подписывается на себя."""
        request = self.context.get('request')
        if request and request.user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        return value

    def validate(self, attrs):
        """Проверяем, что подписка уникальна."""
        request = self.context.get('request')
        if request and Follow.objects.filter(
            user=request.user,
            following=attrs['following']
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя.'
            )
        return attrs
