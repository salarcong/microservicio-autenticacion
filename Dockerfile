# Imagen base mínima
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080 \
    APP_MODULE=${APP_MODULE:-app.main:app}  # cámbialo si tu entrypoint es otro (p.ej. app.wsgi:app)

WORKDIR /app

# Dependencias nativas (ajusta si tu proyecto las necesita)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Instala deps de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código
COPY . .

# Liveness/Readiness (opcional: crea un endpoint /healthz)
# EXPOSE 8080

# Servidor de producción (Gunicorn + UvicornWorker para ASGI)
# Si usas Flask (WSGI), cambia a: CMD ["gunicorn", "app.wsgi:app", "--bind", "0.0.0.0:8080", "--workers", "2"]
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "--workers", "2", "${APP_MODULE}"]
