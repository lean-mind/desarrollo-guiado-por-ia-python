# Reglas del backend — FastAPI

## Validación de input

✓ Usar modelos Pydantic para el body de cada endpoint.
✗ Nunca aceptar `data: dict` sin modelo tipado.

```python
# ✓ Correcto
class CreateMoodRequest(BaseModel):
    mood: str | None = None
    note: str | None = None

@app.post("/add")
def add_mood(data: CreateMoodRequest):
    ...

# ✗ Incorrecto
@app.post("/add")
def add_mood(data: dict):
    mood = data.get("mood", "unknown")
    ...
```

## Separación de responsabilidades

✓ Extraer la lógica de negocio a funciones o clases fuera de las rutas.
✗ No mezclar lógica de negocio directamente en las funciones de ruta.

```python
# ✓ Correcto: función de servicio separada
def create_mood_entry(data: CreateMoodRequest) -> MoodEntry:
    now = datetime.now()
    return MoodEntry(mood=data.mood or "unknown", ...)

@app.post("/add")
def add_mood(data: CreateMoodRequest):
    entry = create_mood_entry(data)
    db.append(entry)
    return {"status": "added", "entry": entry}

# ✗ Incorrecto: todo mezclado en la ruta
@app.post("/add")
def add_mood(data: dict):
    now = datetime.now()
    entry = {"mood": data.get("mood"), "timestamp": now.isoformat(), ...}
    db.append(entry)
    return {"status": "added", "entry": entry}
```

## Tipado

✓ Usar type hints en todas las funciones y modelos de respuesta Pydantic.
✗ No dejar funciones sin tipos de retorno declarados.

## Tests

✓ Cada endpoint tiene su test con `pytest` y `httpx.AsyncClient` o `TestClient`.
✗ No confiar en el servidor de desarrollo para verificar el comportamiento.
