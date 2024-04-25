#!/usr/bin/env sh
set -e

# postgres 5432
while ! nc -z $1 $2; do
      echo "connecting to $1:$2"
      sleep 1
done
python manage.py makemigrations --no-input
python manage.py migrate --no-input
uwsgi --strict --ini uwsgi.ini
