
import tkinter as tk

def add_task():
    task = entry.get()
    deadline = due_date_entry.get()
    if task and deadline:
        task_details = f"Task: {task}    Deadline: {deadline}"
        listbox.insert(tk.END, task_details)
        entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

def mark_as_completed():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        completed_task = task + " [Completed]"
        listbox.delete(index)
        listbox.insert(index, completed_task)
    except:
        pass

def edit_task():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        task_text = task.split("    ")[0].split(": ")[1]
        deadline_text = task.split("    ")[1].split(": ")[1]

        entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        entry.insert(tk.END, task_text)
        due_date_entry.insert(tk.END, deadline_text)

        listbox.delete(index)
    except:
        pass

root = tk.Tk()
root.title("To-Do List")

# Configure colors
bg_color = "pink"  # Background color
button_color = "Red"  # Button color
button_hover_color = "blue"  # Button hover color
listbox_color = "white"  # Listbox color

root.configure(bg=bg_color)

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=75, bg=listbox_color)
listbox.pack(pady=10)

# Create a label for the task entry field
task_label = tk.Label(root, text="Task", bg=bg_color)
task_label.pack()

# Create an entry field for tasks
entry = tk.Entry(root, font=("Times New Roman", 12))
entry.pack(pady=5)

# Create a label for the deadline entry field
due_date_label = tk.Label(root, text="Deadline", bg=bg_color)
due_date_label.pack()

# Create an entry field for due dates
due_date_entry = tk.Entry(root, font=("Times New Roman", 12))
due_date_entry.pack(pady=5)

# Create buttons for adding, editing, marking as completed, and deleting tasks
add_button = tk.Button(root, text="Add Task", command=add_task, bg=button_color, fg="white", activebackground=button_hover_color)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task, bg=button_color, fg="white", activebackground=button_hover_color)
edit_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed, bg=button_color, fg="white", activebackground=button_hover_color)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg=button_color, fg="white", activebackground=button_hover_color)
delete_button.pack(pady=5)

root.mainloop()