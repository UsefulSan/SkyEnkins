# ToDoList_API

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
![redis](https://img.shields.io/badge/-redis-464646?style=flat-square&logo=redis)
![GitHub%20Actions](https://img.shields.io/badge/-celery-464646?style=flat-square&logo=celery)



## Локальный запуск

Клонируйте репозиторий.

Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`, активируйте его (Windows: `venv\scripts\activate`; Linux/Mac: `source venv/bin/activate`), установите зависимости `python -m pip install -r requirements.txt`.
Переименуйте `.env.example` в `.env` и заполните его.

Для локального запуска, находясь в директории проекта выполните команды:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Запуск проекта через Docker

Перейдите в корневую папку проекта, где находится файл `docker-compose.yaml` и выполните команду:

```
docker-compose up --build
```

url - http://localhost:8000/



