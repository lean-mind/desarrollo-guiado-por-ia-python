# Convenciones de commits

Seguimos el formato [Conventional Commits](https://www.conventionalcommits.org/).

## Formato

```
<tipo>(<scope>): <descripción en imperativo>
```

## Tipos

| Tipo | Cuándo usarlo |
|------|--------------|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de bug |
| `test` | Añadir o modificar tests |
| `refactor` | Cambio de código sin añadir funcionalidad ni corregir bug |
| `chore` | Mantenimiento: dependencias, configuración, scripts |
| `docs` | Cambios exclusivamente en documentación |

## Ejemplos

✓ `feat(moods): add DELETE /moods/:id endpoint`
✓ `fix(backend): use Pydantic model instead of raw dict in /add`
✓ `test(moods): add pytest tests for add_mood and list_moods`
✓ `refactor(backend): extract mood logic to service module`
✓ `chore: add ruff and mypy configuration`

✗ `update stuff`
✗ `WIP`
✗ `fixed bug`
✗ `cambios varios`
