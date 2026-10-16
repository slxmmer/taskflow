import json
import os
from task import Task

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return [Task(**d) for d in json.load(f)]
    except Exception:
        return []


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump([t.__dict__ for t in tasks], f, ensure_ascii=False, indent=2)