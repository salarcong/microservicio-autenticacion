FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080 \
    APP_MODULE=app.main:app

WORKDIR /app

# Dependencias del sistema (ajusta si necesitas otras)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Instala deps primero para aprovechar cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir gunicorn

# Copia el resto del código
COPY . .

# Servidor de producción (ASGI con UvicornWorker)
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "--workers", "2", "app.main:app"]
