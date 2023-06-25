import tkinter as tk
from tkinter import messagebox
from tkinter import font

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            messagebox.showinfo("Sucesso", "Tarefa removida com sucesso.")
        else:
            messagebox.showerror("Erro", "Índice inválido. Tarefa não encontrada.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.completed = True
            messagebox.showinfo("Sucesso", "Tarefa marcada como concluída.")
        else:
            messagebox.showerror("Erro", "Índice inválido. Tarefa não encontrada.")

    def display_tasks(self):
        if self.tasks:
            task_list = ""
            for index, task in enumerate(self.tasks):
                status = "Concluída" if task.completed else "Pendente"
                task_list += f"{index}: {task.description} - {status}\n"
            messagebox.showinfo("Lista de Tarefas", task_list)
        else:
            messagebox.showinfo("Lista de Tarefas", "A lista de tarefas está vazia.")

def add_task_button_click():
    description = entry_task.get()
    todo_list.add_task(description)
    entry_task.delete(0, tk.END)

def remove_task_button_click():
    try:
        index = int(entry_index.get())
        todo_list.remove_task(index)
        entry_index.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Índice inválido.")

def complete_task_button_click():
    try:
        index = int(entry_index.get())
        todo_list.complete_task(index)
        entry_index.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Índice inválido.")

def display_tasks_button_click():
    todo_list.display_tasks()

todo_list = TodoList()

window = tk.Tk()
window.title("Aplicativo de Lista de Tarefas")
window.geometry("400x300")
window.configure(bg="black")

font_style = font.Font(family="Arial", size=12)

label_task = tk.Label(window, text="Descrição da Tarefa:", font=font_style, fg="white", bg="black")
label_task.pack()

entry_task = tk.Entry(window, font=font_style)
entry_task.pack()

button_add_task = tk.Button(window, text="Adicionar Tarefa", command=add_task_button_click, font=font_style, fg="white", bg="green")
button_add_task.pack()

label_index = tk.Label(window, text="Índice da Tarefa:", font=font_style, fg="white", bg="black")
label_index.pack()

entry_index = tk.Entry(window, font=font_style)
entry_index.pack()

button_remove_task = tk.Button(window, text="Remover Tarefa", command=remove_task_button_click, font=font_style, fg="white", bg="red")
button_remove_task.pack()

button_complete_task = tk.Button(window, text="Marcar como Concluída", command=complete_task_button_click, font=font_style, fg="white", bg="blue")
button_complete_task.pack()

button_display_tasks = tk.Button(window, text="Exibir Tarefas", command=display_tasks_button_click, font=font_style, fg="white", bg="purple")
button_display_tasks.pack()

window.mainloop()
