# Sandbox-Image für PHP, je Fassung ein eigenes (codeschmiede-sandbox:php-<fassung>, Liste in
# backend/src/codeschmiede/sandbox/laufzeiten.py; das Ausrollen baut sie mit --build-arg PHP_FASSUNG und XDEBUG).
# Gleiche Härtung wie Python; das Programm kommt über stdin (`php` ohne Datei).
ARG PHP_FASSUNG=8.4
FROM php:${PHP_FASSUNG}-cli-alpine
ARG XDEBUG=3.5.3

# Der Dienst ruft `timeout -k`; das BusyBox alter Abbilder (PHP 5.6) kennt -k nicht, dort kommen die coreutils dazu
RUN timeout -k 1 1 true 2>/dev/null || apk add --no-cache coreutils

# Xdebug für den Debugger: gebaut, aber nicht geladen; nur der Aufzeichner startet das Beispiel damit
RUN apk add --no-cache --virtual .bau $PHPIZE_DEPS linux-headers \
 && pecl install "xdebug-${XDEBUG}" \
 && apk del .bau \
 && rm -rf /tmp/pear

WORKDIR /tmp
CMD ["php", "-r", "echo 'codeschmiede-sandbox:php ', PHP_VERSION, ' bereit', PHP_EOL;"]
