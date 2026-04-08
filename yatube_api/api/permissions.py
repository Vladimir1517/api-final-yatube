"""Кастомные пермишены приложения api."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Чтение доступно всем, изменение - только автору."""

    def has_permission(self, request, view):
        """Разграничение доступа на уровне запросов.

        Безопасные запросы доступны всем,
        небезопасные только авторизованным пользователям.
        """
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Разграничение доступа на уровне объекта.
        
        Доступ к объектам по безопасным запросам предоставляется всем,
        небезопасные только автору объекта.
        """
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
