"""Модели приложения posts."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    """Базовая модель с общими полями."""

    text = models.TextField(
        verbose_name='Текст'
    )

    class Meta:
        """Метаданные базовой модели."""

        abstract = True


class Post(BaseModel):
    """Модель поста."""

    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(BaseModel):
    """Модель комментария."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
