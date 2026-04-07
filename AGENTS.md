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
```

## Setup

```bash
# Backend
cd backend && uv sync && make dev

# Frontend
cd frontend && npm install && npm start
```

## Reglas

✓ Usar modelos Pydantic para validar todo input de la API.
✗ Nunca aceptar `data: dict` sin modelo — usar clases Pydantic con tipos explícitos.

✓ Los estilos CSS van en ficheros `.css` separados.
✗ No usar estilos inline en templates de Angular ni en componentes.

✓ Seguir el formato de commits convencionales: `feat:`, `fix:`, `chore:`, `test:`.

## Referencias

- Contexto del backend: `backend/AGENTS.md`
- Contexto del frontend: `frontend/AGENTS.md`
