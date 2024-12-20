#Import Libraries
import tkinter as tk
import json
import os
window = tk.Tk()

#Main Window
window.title("To Do List")
window.geometry("400x500")

#Save Function
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
    print("Tasks saved.")

#Load Function
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            loaded_tasks = json.load(file)
        print("Tasks loaded.")
        return loaded_tasks
    else:
        return []

#Lists
tasks = load_tasks()

#Show To Do Lists
listbox = tk.Listbox(window)


#Show Saved Tasks in Listbox
for task in tasks:
    listbox.insert(tk.END, task)

#Title
label = tk.Label(window, text="To Do List")
label.pack()

#Entry
add_label = tk.Label(window, text="Input Task:")
add_label.pack()
entry = tk.Entry(window)
entry.pack(pady=5)

#Search Tasks
search_label = tk.Label(window, text="Search Task:")
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

#Search Button Function
def search_task():
    search = search_entry.get() #Step 1: Get Search Input
    if search: #Step 2: Check if It's Empty
        for index, each_task in enumerate(tasks):
            if each_task.lower() == search.lower():
                listbox.select_set(index)
                listbox.see(index)
                save_tasks()
                return
            
        print("Task not found.")


#Search Tasks Button
search_button = tk.Button(window, text="Search", command=search_task)
search_button.pack()

#Listbox
listbox.pack(pady=5)

#Button Functions
#Add Function
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

#Delete Function
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        tasks.pop(selected[0])
        save_tasks()

#Mark as Done Function
def completed_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        tasks[task_index] += " (Completed)"
        listbox.delete(task_index)
        listbox.insert(task_index, tasks[task_index])
        save_tasks()

#Clear All Task Function
def clear_task():
    tasks.clear()
    listbox.delete(0, tk.END)
    save_tasks()


#Add Button
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

#Delete Button
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

#Mark as Done Button
complete_button = tk.Button(window, text="Mark as Done", command=completed_task)
complete_button.pack()

#Clear All Task Button
clear_button = tk.Button(window, text="Clear All Task", command=clear_task)
clear_button.pack()


#Run Program
window.mainloop()