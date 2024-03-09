import tkinter as tk
import tkinter.messagebox

task_list = []  # Define the task list here

def entertask():
    # A new window to pop up to take input
    input_text = ""

    def add():
        nonlocal input_text
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tk.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            task_list.append(input_text)
            # close the root1 window
            root1.destroy()
            print_tasks()

    root1 = tk.Toplevel()
    root1.geometry("500x300")  # Set the window size
    root1.title("Add task")
    root1.configure(bg='#F0F0F0')  # Set the background color
    entry_task = tk.Text(root1, width=40, height=10, font=("Arial", 16))
    entry_task.pack(pady=20)
    button_temp = tk.Button(root1, text="Add task", command=add, font=("Arial", 16), bg='#4CAF50', fg='white')
    button_temp.pack()
    root1.mainloop()

def print_tasks():
    listbox_tasks.delete(0, tk.END)
    for i, task in enumerate(task_list):
        listbox_tasks.insert(tk.END, f"{i+1}. {task}")

def removetask():
    task_index_str = entry_index.get()
    if not task_index_str:
        tkinter.messagebox.showwarning(title="Warning!", message="Please enter a task number")
        return
    
    try:
        task_index = int(task_index_str) - 1
        if 0 <= task_index < len(task_list):
            del task_list[task_index]
            print_tasks()
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="Invalid task number")
    except ValueError:
        tkinter.messagebox.showwarning(title="Warning!", message="Invalid task number")
    
    entry_index.delete(0, 'end')  # Clear the entry box after processing

root = tk.Tk()
root.geometry("800x600")  # Set the window size
root.title("To-Do List")
root.configure(bg='#F0F0F0') 
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=20)# Set the background color

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set) 

entry_index = tk.Entry(root, width=3, font=("Arial", 16))
entry_index.pack(pady=20)
button_remove = tk.Button(root, text="Remove task", command=removetask, font=("Arial", 16), bg='#F44336', fg='white')
button_remove.pack()
button_add = tk.Button(root, text="Add task", command=entertask, font=("Arial", 16), bg='#4CAF50', fg='white')
button_add.pack(pady=20)

print_tasks()

root.mainloop()
