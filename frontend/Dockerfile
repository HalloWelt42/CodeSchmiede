# Codeschmiede-Frontend: multi-stage build (Vite -> nginx)

FROM node:22-slim AS build
WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci --no-fund --no-audit

COPY frontend/. ./
COPY VERSION ./VERSION

RUN npm run build

# --- Runtime ---
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8201

CMD ["nginx", "-g", "daemon off;"]
