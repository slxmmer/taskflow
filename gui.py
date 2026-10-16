import tkinter as tk
from tkinter import ttk, messagebox
from task import Task
import storage


class TaskFlowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskFlow")
        self.root.geometry("600x400")

        self.tasks = storage.load_tasks()

        # форма
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="x")

        self.entry = ttk.Entry(frame, width=40)
        self.entry.pack(side="left", padx=5)

        ttk.Button(frame, text="Добавить", command=self.add_task).pack(side="left")

        # список
        self.listbox = tk.Listbox(root)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.refresh()

    def add_task(self):
        title = self.entry.get().strip()
        if not title:
            messagebox.showwarning("Ошибка", "Введите название")
            return
        self.tasks.append(Task(title=title))
        self.entry.delete(0, "end")
        storage.save_tasks(self.tasks)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, "end")
        for t in self.tasks:
            mark = "✓" if t.done else "•"
            self.listbox.insert("end", f"{mark} {t.title} [{t.priority}]")