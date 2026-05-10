FROM python:3.11-slim

# pytest fuer Aufgaben mit komplexen Test-Modulen
RUN pip install --no-cache-dir pytest==8.3.4

# Non-Root-User fuer zusaetzliche Isolation
RUN groupadd -r sandbox && useradd -r -g sandbox sandbox

# Keine .pyc-Dateien (read-only Filesystem zur Laufzeit)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER sandbox
WORKDIR /tmp

# Default zeigt nur, dass das Image laeuft. Der DockerRunner ueberschreibt
# diesen Befehl bei jedem Submission-Lauf.
CMD ["python", "-c", "print('codeschmiede-sandbox bereit')"]
