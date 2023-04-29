# Проект Infra_sp2

### Проект Infra_sp2 предназначен для развертывания в docker-контейнерах с использованием docker-compose приложения Api_Yamdb.  Система состоит из 3-х контейнеров: 1 - Django-проект и сервер Gunicorn; 2 - база данных Postgres; 3 - nginx для раздачи статики.
 
### Шаблон наполнения env-файла:
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=postgres
- POSTGRES_USER=postgres
- POSTGRES_PASSWORD=postgres 
- DB_HOST=db
- DB_PORT=5432 

### Развертывание проекта:
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py createsuperuser
- docker-compose exec web python manage.py collectstatic --no-input 
- docker-compose exec web python manage.py loaddata fixtures.json

## Стек технологий:
```
asgiref==3.2.10
Django==2.2.16
django-filter==2.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.8.0
gunicorn==20.0.4
psycopg2-binary==2.8.6
PyJWT==2.1.0
pytz==2020.1
sqlparse==0.3.1
```
больше в requriments.txt

### Автор

- [Ahmed](https://github.com/ahma09)
