import tkinter as tk
from tkinter import messagebox

# add task with checkbox
def add_task():
    task = entry.get()
    if task != "":
        var = tk.IntVar()
        task_frame = tk.Frame(listbox, bg="#ffd8eb", pady=5)

        checkbox = tk.Checkbutton(task_frame, text=task, variable=var, onvalue=1, offvalue=0, font=("Helvetica", 14), bg="#ffd8eb", fg="#333333", command=lambda: complete_task(var, checkbox))
        checkbox.pack(side=tk.LEFT, padx=10)

        task_frame.pack(fill=tk.X, pady=2)
        tasks.append((var, checkbox))
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠︎ warning! ⚠︎", "you must enter a task.")

# marks task as completed
# when completed, task gets striked through and disappears
def complete_task(var, checkbox):
    if var.get() == 1:  # Check if checkbox is selected
        checkbox.config(fg="#999999", font=("Helvetica", 14, "overstrike"))
        checkbox.master.after(600, lambda: checkbox.master.pack_forget())  # hide the task after a short delay
        check_all_completed()

# check if all tasks are completed
def check_all_completed():
    if all(var.get() for var, _ in tasks):
        show_confetti()

# delete all tasks after confirmation by the user
def delete_all_tasks():
    if messagebox.askyesno("confirm", "do you really want to delete all tasks?"):
        for widget in listbox.winfo_children():
            widget.destroy()
        tasks.clear()

# shows confetti after all tasks are completed
def show_confetti():
    confetti_label = tk.Label(root, text="🎉 all tasks completed! 🎉", font=("Helvetica", 18), bg="#FFFFFF", fg="#f090a2")
    # Center the label in the window
    confetti_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    root.after(2000, confetti_label.place_forget)

# main application window
root = tk.Tk()
root.title("to-do list! ♡")
root.geometry("400x500")

# load and set background image
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# title of window
title_label = tk.Label(root, text="⋆₊˚♡ to-do list ₊˚✩⊹", font=("Helvetica", 18, "bold"), bg="#FFFFFF", fg="#f090a2")
title_label.pack(pady=20)

# create a frame to hold the task entry box and add button
entry_frame = tk.Frame(root, bg="#FFFFFF")
entry_frame.pack(pady=10)

# create an input field where users can type in their task
entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=20, bd=2, relief=tk.SOLID, highlightbackground="#f090a2", highlightcolor="#f090a2", highlightthickness=2)
entry.grid(row=0, column=0, padx=10)

# create a button to add tasks
add_button = tk.Button(entry_frame, text="add", font=("Helvetica", 12), bg="#f090a2", fg="#FFFFFF", width=10, bd=0, command=add_task)
add_button.grid(row=0, column=1)

# frame to hold tasks with checkboxes
listbox = tk.Frame(root, bg="#FFFFFF")
listbox.pack(pady=20, fill=tk.BOTH, expand=True)

tasks = []

# buttons for task actions
button_frame = tk.Frame(root, bg="#FFFFFF")
button_frame.pack(pady=10)

# create a delete all button that deletes all tasks
delete_all_button = tk.Button(button_frame, text="delete all", font=("Helvetica", 12), bg="#FA4166", fg="#FFFFFF", width=10, bd=0, command=delete_all_tasks)
delete_all_button.grid(row=0, column=0, padx=5)

# start the main loop
root.mainloop()
