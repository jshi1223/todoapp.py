import tkinter as tk
from tkinter import messagebox, filedialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Entry for new task
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # Add task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Task listbox
        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Delete task button
        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_task)
        self.delete_button.pack()

        # Save and Load buttons
        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(side=tk.RIGHT, padx=20, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Select Error", "Please select a task to delete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                for task in self.tasks:
                    f.write(task + "\n")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
                self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
