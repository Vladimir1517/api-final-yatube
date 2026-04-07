"""Кастомные пагинаторы приложения api."""
from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """Условная пагинация с параметрами limit и offset."""

    def paginate_queryset(self, queryset, request, view=None):
        """Применяет пагинацию только при наличии limit/offset в запросе."""
        limit = self.get_limit(request)
        offset = self.get_offset(request)

        if limit is None and offset == 0:
            return None
        return super().paginate_queryset(queryset, request, view)
