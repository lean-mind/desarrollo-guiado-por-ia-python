# Red-Green-Refactor: Ejemplos en Python/pytest

## Ejemplo: endpoint DELETE /moods/{id}

### Red — test que falla

```python
def test_delete_mood_returns_deleted_status(self) -> None:
    response = client.post("/add", json={"mood": "happy"})
    mood_id = response.json()["entry"]["id"]

    response = client.delete(f"/delete/{mood_id}")

    assert response.status_code == 200
    assert response.json() == {"status": "deleted", "id": mood_id}
```

Ejecuta: `uv run pytest` → **FAIL** (endpoint no existe, 404)

### Green — código mínimo

```python
@app.delete("/delete/{mood_id}")
def delete_mood(mood_id: int) -> dict[str, Any]:
    global db
    db = [m for m in db if m["id"] != mood_id]
    return {"status": "deleted", "id": mood_id}
```

Ejecuta: `uv run pytest` → **PASS**

### Refactor — mejoras sin cambiar comportamiento

```python
@app.delete("/delete/{mood_id}")
def delete_mood(mood_id: int) -> dict[str, Any]:
    original_count = len(db)
    db[:] = [m for m in db if m["id"] != mood_id]
    if len(db) == original_count:
        raise HTTPException(status_code=404, detail=f"Mood {mood_id} not found")
    return {"status": "deleted", "id": mood_id}
```

Ejecuta: `uv run pytest` → **PASS** (añadir test para 404 en siguiente ciclo)

## Anti-patrones a evitar

| Anti-patrón | Correcto |
|-------------|----------|
| Escribir 5 tests antes del código | Un test → código → siguiente test |
| Test que pasa sin haber escrito código | El test debe fallar primero |
| Refactor que añade funcionalidad | Refactor solo mejora estructura |
| Skip del refactor | Siempre refactorizar antes del commit |
