# Проект Infra_sp2

### Проект Infra_sp2 предназначен для развертывания в docker-контейнерах с использованием docker-compose приложения Api_Yamdb.  
Система состоит из 3-х контейнеров:
- Django-проект и сервер Gunicorn;
- База данных PostgreSQL;
- Nginx для раздачи статики.
 
### Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres 
DB_HOST=db
DB_PORT=5432 
```
### Развертывание проекта:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
docker-compose exec web python manage.py loaddata fixtures.json
```
## Стек технологий:
```
Python
Django
Django Rest Framework
PostgreSQL
Docker
Docker-Compose
Nginx
Gunicorn
```
### Автор
[Ahmed](https://github.com/ahma09)
