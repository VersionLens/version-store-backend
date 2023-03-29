#!/bin/sh

cp -r /app/* /code
cd /code/django
python manage.py migrate --no-input
DJANGO_SUPERUSER_USERNAME=demo DJANGO_SUPERUSER_EMAIL=foo@bar.com DJANGO_SUPERUSER_PASSWORD=demo python manage.py createsuperuser --no-input
exec python manage.py runserver 0.0.0.0:8000
