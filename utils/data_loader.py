import json
from pathlib import Path

def load_data():
    path = Path(__file__).resolve().parents[1] / "data" / "test_data.json"
    with path.open(encoding="utf-8") as file:
        return json.load(file)
