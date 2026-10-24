# Sandbox-Image für Python-Aufgaben. Der Sandbox-Dienst startet es mit
# fremdem Nutzer (nobody), ohne Netz, nur lesend, und reicht das
# Programm über stdin hinein (`python -`).
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /tmp
CMD ["python", "-c", "print('codeschmiede-sandbox:python bereit')"]
