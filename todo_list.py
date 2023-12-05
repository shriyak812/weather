from tkinter import *
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = Tk()
root.title("To-Do List App")
root.geometry("400x300")

# Create and place widgets
label = Label(root, text="To-Do List", font=("Helvetica", 20, "bold"))
label.pack(pady=10)

entry = Entry(root, font=("Arial", 14))
entry.pack(pady=10)

add_button = Button(root, text="Add Task", command=add_task, font=("Arial", 12))
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task", command=delete_task, font=("Arial", 12))
delete_button.pack(pady=5)

listbox = Listbox(root, selectmode=SINGLE, font=("Arial", 12), selectbackground="#a6a6a6")
listbox.pack(pady=10, fill=BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()
