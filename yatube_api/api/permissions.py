"""Кастомные пермишены приложения api."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Чтение доступно всем, изменение - только автору."""

    def has_permission(self, request, view):
        """
        Безопасные запросы доступны всем,
        небезопасные только авторизованным пользователям.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Доступ к объектам по безопасным запросам предоставляется всем,
        небезопасные только автору объекта.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
