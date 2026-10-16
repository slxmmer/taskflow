"""
TaskFlow — умный список дел с приоритетами.
"""
import tkinter as tk
from gui import TaskFlowApp


def main():
    root = tk.Tk()
    app = TaskFlowApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()