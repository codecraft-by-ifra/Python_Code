import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

FILE_NAME = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced To-Do List")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.filtered_tasks = []

        # ---------------- Title ----------------
        title = ttk.Label(root, text="To-Do List", font=("Helvetica", 20, "bold"))
        title.pack(pady=10)

        # ---------------- Input Frame ----------------
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=10, padx=10, fill="x")

        self.task_entry = ttk.Entry(input_frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.date_entry = ttk.Entry(input_frame, width=15)
        self.date_entry.grid(row=0, column=1, padx=5)
        self.date_entry.insert(0, "YYYY-MM-DD")

        add_button = ttk.Button(input_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=2, padx=5)

        # ---------------- Search ----------------
        search_frame = ttk.Frame(root)
        search_frame.pack(pady=5, padx=10, fill="x")

        ttk.Label(search_frame, text="Search:").pack(side="left")
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.search_entry.bind("<KeyRelease>", self.search_task)

        # ---------------- Task List ----------------
        columns = ("Task", "Due Date", "Status")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        self.tree.heading("Task", text="Task")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.heading("Status", text="Status")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # ---------------- Buttons ----------------
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Mark Completed", command=self.mark_completed).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).grid(row=0, column=2, padx=5)

        # Load tasks from file
        self.load_tasks()

    # ---------------- Add Task ----------------
    def add_task(self):
        task = self.task_entry.get().strip()
        due_date = self.date_entry.get().strip()

        if not task:
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return

        try:
            if due_date and due_date != "YYYY-MM-DD":
                datetime.strptime(due_date, "%Y-%m-%d")
            else:
                due_date = ""
        except ValueError:
            messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD.")
            return

        new_task = {"task": task, "due_date": due_date, "status": "Pending"}
        self.tasks.append(new_task)
        self.save_tasks()
        self.update_tree()

        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, "YYYY-MM-DD")

    # ---------------- Update Treeview ----------------
    def update_tree(self, tasks=None):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if tasks is None:
            tasks = self.tasks

        for task in tasks:
            self.tree.insert("", tk.END, values=(task["task"], task["due_date"], task["status"]))

    # ---------------- Mark Completed ----------------
    def mark_completed(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task.")
            return

        for item in selected:
            values = self.tree.item(item, "values")
            for task in self.tasks:
                if task["task"] == values[0] and task["due_date"] == values[1]:
                    task["status"] = "Completed"

        self.save_tasks()
        self.update_tree()

    # ---------------- Delete Task ----------------
    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task.")
            return

        for item in selected:
            values = self.tree.item(item, "values")
            self.tasks = [
                task for task in self.tasks
                if not (task["task"] == values[0] and task["due_date"] == values[1])
            ]

        self.save_tasks()
        self.update_tree()

    # ---------------- Clear All Tasks ----------------
    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.save_tasks()
            self.update_tree()

    # ---------------- Search Tasks ----------------
    def search_task(self, event):
        query = self.search_entry.get().lower()
        self.filtered_tasks = [
            task for task in self.tasks
            if query in task["task"].lower()
        ]
        self.update_tree(self.filtered_tasks)

    # ---------------- Save Tasks ----------------
    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # ---------------- Load Tasks ----------------
    def load_tasks(self):
        try:
            with open(FILE_NAME, "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
        self.update_tree()

# ---------------- Run Application ----------------
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")  # You can try 'default', 'alt', or 'vista'
    app = TodoApp(root)
    root.mainloop()