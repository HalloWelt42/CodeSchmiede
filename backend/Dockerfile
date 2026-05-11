# Codeschmiede-Backend: FastAPI + uvicorn + docker-CLI
# (der Container braucht docker-CLI, um Sandbox-Container fuer Submissions
# zu starten; der Daemon-Socket wird via volume-Mount eingehaengt)

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
      docker.io \
      curl \
    && rm -rf /var/lib/apt/lists/*

# Erst Sourcen + pyproject zusammen kopieren -- pyproject.toml verweist
# auf packages.find: src, daher MUSS src/ existieren bevor pip install
# gestartet wird (sonst 'src does not exist' im egg_info-Schritt).
COPY backend/pyproject.toml ./
COPY backend/src ./src
COPY VERSION ./VERSION

RUN pip install --no-cache-dir uv \
    && uv pip install --system .

ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

EXPOSE 8200

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -fsS http://localhost:8200/api/healthz || exit 1

CMD ["python", "-m", "uvicorn", "codeschmiede.api:app_bauen", \
     "--factory", "--host", "0.0.0.0", "--port", "8200"]
