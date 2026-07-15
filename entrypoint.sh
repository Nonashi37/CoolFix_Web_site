#!/bin/sh
set -e

echo "═══ Применяем миграции ═══"
python manage.py migrate --noinput

echo "═══ Собираем статику ═══"
python manage.py collectstatic --noinput --clear

echo "═══ Запускаем Gunicorn ═══"
exec "$@"