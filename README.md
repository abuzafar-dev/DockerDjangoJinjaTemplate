# Docker + Django Jinja Template

Django + Jinja2 loyihasi Docker ichida, PostgreSQL bilan. Misol sifatida vazifalar ro'yxati (todo): qo'shish, bajarildi deb belgilash, o'chirish.

## Quick start

```bash
make run     # creates .venv and .env, installs deps, starts the app
make test    # checks + tests
```

## Docker bilan ishga tushirish

```bash
cp .env.example .env
docker compose up --build
```

http://127.0.0.1:8000/

Superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

## Tuzilishi

- `Dockerfile` — python:3.12-slim, gunicorn
- `entrypoint.sh` — `migrate` va `collectstatic`
- `docker-compose.yml` — `web` va `db` (postgres:16) servislari
- `config/jinja2.py` — Jinja2 muhiti

## Testlar

```bash
docker compose exec web python manage.py test
```
