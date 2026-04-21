# Mood Tracker — Python

Aplicación de seguimiento de estados de ánimo. Monorepo con backend en FastAPI y frontend en Angular.

## Stack

| Capa | Tecnología | Versión |
|------|-----------|---------|
| Backend | Python | 3.14+ |
| Backend | FastAPI | >= 0.104.0 |
| Backend | UV | latest |
| Frontend | Angular | 21 |
| Frontend | TypeScript | 5.9 |
| Frontend | Node.js | v24 |

## Estructura

```
backend/    # API FastAPI (puerto 8000)
frontend/   # Aplicación Angular (puerto 4200)
docs/       # Reglas y convenciones globales del proyecto
```

## Setup

```bash
# Backend
cd backend && uv sync && make dev

# Frontend
cd frontend && npm install && npm start
```

## Reglas globales

Ver `docs/commits.md` para convenciones de commits.
