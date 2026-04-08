from datetime import datetime
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db: list[dict[str, Any]] = []


class CreateMoodRequest(BaseModel):
    mood: str | None = Field(default=None, max_length=100)
    note: str | None = Field(default=None, max_length=500)


@app.post("/add")
def add_mood(data: CreateMoodRequest) -> dict[str, Any]:
    mood_entry: dict[str, Any] = {
        "id": len(db) + 1,
        "mood": data.mood or "unknown",
        "note": data.note or "",
        "timestamp": datetime.now().isoformat(),
        "date_formatted": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "day_of_week": datetime.now().strftime("%A"),
        "is_weekend": datetime.now().weekday() >= 5,
    }
    db.append(mood_entry)
    return {"status": "added", "entry": mood_entry}


@app.get("/list")
def list_moods() -> dict[str, Any]:
    sorted_db = sorted(db, key=lambda x: x["timestamp"], reverse=True)
    for item in sorted_db:
        item["age_in_seconds"] = (
            datetime.now() - datetime.fromisoformat(item["timestamp"])
        ).total_seconds()
    return {"moods": sorted_db, "count": len(sorted_db)}
