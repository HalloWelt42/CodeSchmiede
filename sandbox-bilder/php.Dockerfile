# Sandbox-Image für PHP, je Fassung ein eigenes (codeschmiede-sandbox:php-<fassung>, Liste in
# backend/src/codeschmiede/sandbox/laufzeiten.py; das Ausrollen baut sie mit --build-arg PHP_FASSUNG).
# Gleiche Härtung wie Python; das Programm kommt über stdin (`php` ohne Datei).
ARG PHP_FASSUNG=8.4
FROM php:${PHP_FASSUNG}-cli-alpine

WORKDIR /tmp
CMD ["php", "-r", "echo 'codeschmiede-sandbox:php ', PHP_VERSION, ' bereit', PHP_EOL;"]
