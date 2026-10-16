from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    title: str
    priority: str = "средний"
    deadline: str = ""
    done: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def sort_key(self):
        return (self.done, self.priority, self.deadline)