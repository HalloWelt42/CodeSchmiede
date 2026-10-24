# Sandbox-Image für JavaScript-Aufgaben. Gleiche Härtung wie Python;
# das Programm kommt über stdin (`node -`).
FROM node:26-slim

ENV NODE_ENV=production

WORKDIR /tmp
CMD ["node", "-e", "console.log('codeschmiede-sandbox:javascript bereit')"]
