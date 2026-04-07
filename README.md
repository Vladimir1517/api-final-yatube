# API для Yatube

REST API для социальной сети Yatube. Проект реализует функциональность для работы с постами, комментариями, группами и подписками.

## 📌 Описание

API позволяет:

* создавать, редактировать и удалять посты
* добавлять комментарии
* подписываться на авторов
* просматривать группы
* работать с пользователями через JWT-аутентификацию

Проект построен на Django REST Framework и соответствует REST-архитектуре.

---

## ⚙️ Технологии

* Python 3.x
* Django
* Django REST Framework
* JWT (JSON Web Token)
* SQLite
* Pytest

---

## 🚀 Установка

Клонировать репозиторий:

```bash
git clone https://github.com/Vladimir1517/api-final-yatube.git
cd api-final-yatube
```

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать:

```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Применить миграции:

```bash
python manage.py migrate
```

Запустить сервер:

```bash
python manage.py runserver
```

---

## 🔐 Аутентификация

Получение токена:

```
POST /api/v1/jwt/create/
```

Обновление токена:

```
POST /api/v1/jwt/refresh/
```

Проверка токена:

```
POST /api/v1/jwt/verify/
```

---

## 📡 Эндпоинты

* GET `/api/v1/posts/` — список постов

* POST `/api/v1/posts/` — создать пост

* GET `/api/v1/posts/{id}/` — получить пост

* PUT/PATCH `/api/v1/posts/{id}/` — обновить пост

* DELETE `/api/v1/posts/{id}/` — удалить пост

* GET `/api/v1/groups/` — список групп

* GET `/api/v1/comments/` — комментарии

* GET `/api/v1/follow/` — подписки

---

## 🔎 Пример запроса

Создание поста:

```json
{
  "text": "Мой первый пост",
  "group": 1
}
```

Пример ответа:

```json
{
  "id": 1,
  "text": "Мой первый пост",
  "author": "username",
  "pub_date": "2025-01-01T12:00:00Z"
}
```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 📂 Структура проекта

```
api_final_yatube/
├── yatube_api/
├── tests/
├── requirements.txt
├── manage.py
└── README.md
```

---

## 👤 Автор

Vladimir Tyutin

---

## 📄 Лицензия

Проект используется в учебных целях.
