#!/bin/sh
set -e

su $USER

# collect static
python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate

gunicorn app.wsgi:application --bind 0.0.0.0:8000

exec "$@"
