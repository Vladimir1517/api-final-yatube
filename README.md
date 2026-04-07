# API для Yatube

[![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.12+-green.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

RESTful API для блог-платформы Yatube. Проект предоставляет возможности для создания постов, комментариев, управления группами и подписками на авторов.

## 🚀 Возможности

- **Посты**: создание, редактирование, удаление и просмотр публикаций
- **Комментарии**: полноценное обсуждение под каждым постом
- **Группы**: тематические сообщества для постов
- **Подписки**: система Follow на интересных авторов
- **Аутентификация**: JWT-токены для безопасного доступа
- **Пагинация**: удобная навигация по большим спискам

## 🛠 Технологии

- Python 3.7+
- Django 3.2
- Django REST Framework 3.12
- Simple JWT (аутентификация)
- SQLite3 (разработка) / PostgreSQL (продакшн)

## 📦 Установка и запуск

### Клонирование репозитория
```bash
git clone https://github.com/Vladimir1517/api-final-yatube.git
cd api-final-yatube
Создание виртуального окружения
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
Установка зависимостей
bash
pip install -r requirements.txt
Применение миграций
bash
python manage.py migrate
Создание суперпользователя (опционально)
bash
python manage.py createsuperuser
Запуск сервера разработки
bash
python manage.py runserver
API будет доступен по адресу: http://127.0.0.1:8000/api/v1/

🔑 Аутентификация
Проект использует JWT-токены. Получите токены через эндпоинты:

Эндпоинт	Метод	Описание
/api/v1/jwt/create/	POST	Получение access и refresh токенов
/api/v1/jwt/refresh/	POST	Обновление access токена
/api/v1/jwt/verify/	POST	Проверка токена
Пример запроса для получения токена:

json
{
  "username": "your_username",
  "password": "your_password"
}
Далее передавайте access-токен в заголовке:

text
Authorization: Bearer <ваш_access_токен>
📚 Эндпоинты API
Все эндпоинты доступны с префиксом /api/v1/

Посты (/posts/)
Метод	URL	Описание
GET	/posts/	Список всех постов (пагинация)
POST	/posts/	Создать новый пост
GET	/posts/{id}/	Получить пост по ID
PUT	/posts/{id}/	Полностью обновить пост
PATCH	/posts/{id}/	Частично обновить пост
DELETE	/posts/{id}/	Удалить пост
Комментарии (/posts/{post_id}/comments/)
Метод	URL	Описание
GET	/posts/{post_id}/comments/	Список комментариев к посту
POST	/posts/{post_id}/comments/	Добавить комментарий
GET	/posts/{post_id}/comments/{id}/	Получить комментарий
PUT/PATCH	/posts/{post_id}/comments/{id}/	Редактировать комментарий
DELETE	/posts/{post_id}/comments/{id}/	Удалить комментарий
Группы (/groups/)
Метод	URL	Описание
GET	/groups/	Список всех групп
GET	/groups/{id}/	Информация о группе
Подписки (/follow/)
Метод	URL	Описание
GET	/follow/	Список авторов, на которых подписан
POST	/follow/	Подписаться на автора
Примечание: Для /follow/ требуется передавать following (username автора) в теле запроса.

📝 Примеры запросов
Создание поста
bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Мой первый пост!", "group": 1}'
Получение списка постов с пагинацией
bash
curl "http://127.0.0.1:8000/api/v1/posts/?limit=5&offset=10"
Подписка на автора
bash
curl -X POST http://127.0.0.1:8000/api/v1/follow/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"following": "ivanov"}'
🧪 Тестирование
Для запуска тестов:

bash
python manage.py test
📁 Структура проекта
text
api-final-yatube/
├── api/                # Приложение API
│   ├── permissions.py  # Права доступа
│   ├── serializers.py  # Сериализаторы DRF
│   ├── views.py        # Представления (ViewSets)
│   └── urls.py         # Маршруты API
├── posts/              # Основное приложение блога
│   ├── models.py       # Модели Post, Group, Comment, Follow
│   └── admin.py        # Настройка админ-панели
├── yatube_api/         # Настройки проекта Django
├── requirements.txt    # Зависимости проекта
└── manage.py
📄 Лицензия
MIT

👤 Автор
Vladimir1517 — GitHub