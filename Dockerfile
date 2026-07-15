FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --system django && useradd --system --create-home --gid django django

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=django:django . .

# ─── ФИКС ───────────────────────────────────────────────────────────────
# Создаём папку и отдаём её django:django ДО переключения на non-root юзера.
# Механика: Docker при ПЕРВОМ монтировании именованного volume на путь,
# который уже существует в образе, копирует содержимое (и владельца!) этой
# папки из образа В volume. Если папки не будет — Docker создаст volume
# пустым и root-owned, и мы вернёмся к той же ошибке.
RUN mkdir -p /app/staticfiles && chown -R django:django /app/staticfiles

USER django

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "coolfix.wsgi:application", "--config", "gunicorn.conf.py"]