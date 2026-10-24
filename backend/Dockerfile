# Codeschmiede: ein Python-Unterbau, zwei Ziele.
#   backend  -- FastAPI-App, ohne Docker-Zugang
#   sandbox  -- Sandbox-Dienst, einziger Teil mit Docker-CLI und Socket
# Bauen: docker compose build (die Ziele stehen in docker-compose.yml).

FROM python:3.14-slim AS basis

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Installiert wird genau nach der Sperrdatei (uv.lock), ohne Entwicklerpakete:
# erst die Abhängigkeiten (eigene Schicht), dann das Projekt.
COPY --from=ghcr.io/astral-sh/uv:0.11.7 /uv /usr/local/bin/uv
ENV UV_PROJECT_ENVIRONMENT=/usr/local UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
COPY backend/pyproject.toml backend/uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project
COPY backend/src ./src
COPY VERSION ./VERSION
RUN uv sync --frozen --no-dev --no-editable

ENV PYTHONUNBUFFERED=1


FROM basis AS backend

EXPOSE 8200
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -fsS http://localhost:8200/api/healthz || exit 1
CMD ["python", "-m", "uvicorn", "codeschmiede.api:app_bauen", \
     "--factory", "--host", "0.0.0.0", "--port", "8200"]


FROM basis AS sandbox

# Nur die Kommandozeile; der Daemon ist der des Hosts (Socket im Compose)
RUN apt-get update && apt-get install -y --no-install-recommends docker-cli \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8203
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -fsS http://localhost:8203/gesund || exit 1
CMD ["python", "-m", "codeschmiede.sandbox.dienst"]
