# Codeschmiede: ein Python-Unterbau, zwei Ziele.
#   backend  -- FastAPI-App, ohne Docker-Zugang
#   sandbox  -- Sandbox-Dienst, einziger Teil mit Docker-CLI und Socket
# Bauen: docker compose build (die Ziele stehen in docker-compose.yml).

FROM python:3.11-slim AS basis

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# pyproject verweist auf packages.find: src, darum src vor der Installation kopieren.
COPY backend/pyproject.toml ./
COPY backend/src ./src
COPY VERSION ./VERSION

RUN pip install --no-cache-dir uv \
    && uv pip install --system .

ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1


FROM basis AS backend

EXPOSE 8200
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -fsS http://localhost:8200/api/healthz || exit 1
CMD ["python", "-m", "uvicorn", "codeschmiede.api:app_bauen", \
     "--factory", "--host", "0.0.0.0", "--port", "8200"]


FROM basis AS sandbox

RUN apt-get update && apt-get install -y --no-install-recommends docker.io \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8203
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -fsS http://localhost:8203/gesund || exit 1
CMD ["python", "-m", "codeschmiede.sandbox.dienst"]
