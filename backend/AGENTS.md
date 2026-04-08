# Backend — FastAPI

API REST construida con FastAPI. Almacenamiento en memoria (datos se pierden al reiniciar).

## Endpoints

| Método | Ruta | Body | Respuesta |
|--------|------|------|-----------|
| POST | `/add` | `{ mood?: string, note?: string }` | `{ status: str, entry: dict }` |
| GET | `/list` | — | `{ moods: list, count: int }` |
| DELETE | `/delete/{id}` | — | `{ status: str, id: int }` |

## Arquitectura

```
main.py         # Aplicación FastAPI: endpoints, lógica, almacenamiento en memoria (db = [])
pyproject.toml  # Dependencias declaradas (gestionadas con UV)
Makefile        # Comandos de desarrollo
```

## Reglas

Ver `docs/reglas.md` para las convenciones del backend.

## Comandos

```bash
make dev                    # Servidor de desarrollo con hot reload
uv run fastapi dev main.py  # Equivalente manual
uv run pytest               # Ejecutar tests
uv run ruff check .         # Linter
uv run mypy .               # Type checker
```
