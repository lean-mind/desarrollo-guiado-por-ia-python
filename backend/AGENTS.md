# Backend — FastAPI

API REST construida con FastAPI. Almacenamiento en memoria (datos se pierden al reiniciar).

## Endpoints

| Método | Ruta | Body | Respuesta |
|--------|------|------|-----------|
| POST | `/add` | `{ mood?: string, note?: string }` | `{ status: str, entry: dict }` |
| GET | `/list` | — | `{ moods: list, count: int }` |

## Arquitectura

```
main.py         # Aplicación FastAPI completa: endpoints, lógica, almacenamiento en memoria
pyproject.toml  # Dependencias declaradas (gestionadas con UV)
Makefile        # Comandos de desarrollo
```

## Reglas

✓ Usar modelos Pydantic para el body de cada endpoint.
✗ No aceptar `data: dict` sin modelo — definir siempre una clase Pydantic con tipos explícitos.

✓ Separar la lógica de negocio de los endpoints (funciones o clases de servicio).
✗ No mezclar lógica de negocio directamente en las funciones de ruta.

✓ Añadir tests para cada endpoint con `pytest`.

## Comandos

```bash
make dev                    # Servidor de desarrollo con hot reload
uv run fastapi dev main.py  # Equivalente manual
uv run pytest               # Ejecutar tests
uv run ruff check .         # Linter
uv run mypy .               # Type checker
```
