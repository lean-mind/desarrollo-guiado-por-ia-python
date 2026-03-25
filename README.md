# Mood Tracker

Prototipo de seguimiento de estados de ánimo construido como monorepo con backend en Python (FastAPI) y frontend en Angular.

## Estructura del proyecto

```
.
├── backend/               # API REST con FastAPI
│   ├── main.py            # Endpoints /add y /list
│   ├── pyproject.toml     # Dependencias (gestionadas con UV)
│   ├── Makefile           # Comando de desarrollo
│   └── .python-version    # Versión de Python (3.14.2)
└── frontend/              # Aplicación Angular
    ├── src/
    │   ├── index.html
    │   ├── main.ts
    │   └── app/
    │       └── app.component.ts
    ├── angular.json
    ├── package.json
    └── .nvmrc             # Versión de Node (v24.11.1)
```

## Requisitos previos

### Backend
- **Python 3.14+** — se recomienda usar [pyenv](https://github.com/pyenv/pyenv) y respetar el `.python-version`
- **UV** — gestor de paquetes de Python

```bash
# Instalar UV
curl -Ls https://astral.sh/uv/install.sh | sh
```

### Frontend
- **Node.js v24.11.1** — se recomienda usar [nvm](https://github.com/nvm-sh/nvm) y respetar el `.nvmrc`

```bash
# Instalar la versión de Node indicada en .nvmrc
cd frontend
nvm use
```

## Instalación

### Backend

```bash
cd backend
uv sync
```

Esto crea el entorno virtual `.venv` e instala todas las dependencias declaradas en `pyproject.toml`.

### Frontend

```bash
cd frontend
npm install
```

## Levantar el proyecto

El proyecto requiere dos terminales abiertas en paralelo, una para cada servicio.

### Terminal 1 — Backend

```bash
cd backend
make dev
```

O de forma manual:

```bash
cd backend
uv run fastapi dev main.py
```

El servidor quedará disponible en **http://localhost:8000**

### Terminal 2 — Frontend

```bash
cd frontend
npm start
```

La aplicación quedará disponible en **http://localhost:4200**

## Tecnologías

| Capa | Tecnología | Versión |
|---|---|---|
| Backend | Python | 3.14.2 |
| Backend | FastAPI | >= 0.104.0 |
| Backend | Uvicorn | >= 0.24.0 |
| Backend | UV | latest |
| Frontend | Angular | 21.1.2 |
| Frontend | TypeScript | 5.9.3 |
| Frontend | Node.js | v24.11.1 |
| Frontend | RxJS | 7.8.1 |

## Notas

- El backend usa una **lista en memoria** como almacenamiento. Los datos se pierden al reiniciar el servidor.
- CORS está habilitado para todos los orígenes (`*`), pensado exclusivamente para desarrollo local.
- La URL del backend está hardcodeada en `frontend/src/app/app.component.ts` como `http://localhost:8000`.
