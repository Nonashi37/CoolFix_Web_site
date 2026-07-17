FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --system django && useradd --system --gid django django

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=django:django . .

RUN mkdir -p /app/staticfiles && chown -R django:django /app/staticfiles

# ФИКС: сама папка /app была создана WORKDIR ещё от root, ДО того как
# появился django-юзер. COPY --chown красит только содержимое, а не
# родительскую директорию. SQLite создаёт -journal файл РЯДОМ с базой
# при любой записи — значит нужны права на запись именно в саму папку,
# не только в файл db.sqlite3 внутри неё.
RUN chown django:django /app

USER django

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "coolfix.wsgi:application", "--config", "gunicorn.conf.py"]