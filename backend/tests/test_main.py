import pytest
from fastapi.testclient import TestClient
from main import app, db

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    db.clear()
    yield
    db.clear()


class TestAddMood:
    def test_add_mood_with_all_fields(self):
        response = client.post("/add", json={"mood": "happy", "note": "great day"})

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "added"
        assert data["entry"]["mood"] == "happy"
        assert data["entry"]["note"] == "great day"

    def test_add_mood_without_mood_defaults_to_unknown(self):
        response = client.post("/add", json={})

        assert response.status_code == 200
        assert response.json()["entry"]["mood"] == "unknown"

    def test_add_mood_without_note_defaults_to_empty_string(self):
        response = client.post("/add", json={"mood": "happy"})

        assert response.status_code == 200
        assert response.json()["entry"]["note"] == ""

    def test_add_mood_with_invalid_type_returns_422(self):
        response = client.post("/add", json={"mood": 123})

        assert response.status_code == 422

    def test_add_mood_exceeding_max_length_returns_422(self):
        response = client.post("/add", json={"mood": "x" * 101})

        assert response.status_code == 422

    def test_add_mood_includes_required_fields(self):
        response = client.post("/add", json={"mood": "ok"})
        entry = response.json()["entry"]

        assert "id" in entry
        assert "timestamp" in entry
        assert "date_formatted" in entry
        assert "day_of_week" in entry
        assert "is_weekend" in entry


class TestListMoods:
    def test_list_moods_empty_initially(self):
        response = client.get("/list")

        assert response.status_code == 200
        data = response.json()
        assert data["moods"] == []
        assert data["count"] == 0

    def test_list_moods_returns_all_added_entries(self):
        client.post("/add", json={"mood": "happy"})
        client.post("/add", json={"mood": "sad"})

        response = client.get("/list")
        data = response.json()

        assert data["count"] == 2
        assert len(data["moods"]) == 2

    def test_list_moods_includes_age_in_seconds(self):
        client.post("/add", json={"mood": "ok"})

        response = client.get("/list")
        mood = response.json()["moods"][0]

        assert "age_in_seconds" in mood
        assert mood["age_in_seconds"] >= 0

    def test_list_moods_sorted_by_timestamp_descending(self):
        import time
        client.post("/add", json={"mood": "first"})
        time.sleep(0.01)
        client.post("/add", json={"mood": "second"})

        response = client.get("/list")
        moods = response.json()["moods"]

        assert moods[0]["mood"] == "second"
        assert moods[1]["mood"] == "first"
