FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .
# ENV SECRET_KEY='p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs'


CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]