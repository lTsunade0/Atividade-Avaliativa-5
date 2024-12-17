import tkinter as tk
from tkinter import messagebox


tarefas = []


def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    categoria = entrada_categoria.get()
    prioridade = entrada_prioridade.get()
    
    if tarefa and categoria and prioridade:
        
        tarefas.append({"tarefa": tarefa, "categoria": categoria, "prioridade": prioridade})
        atualizar_lista()
        entrada_tarefa.delete(0, tk.END)
        entrada_categoria.delete(0, tk.END)
        entrada_prioridade.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira todos os detalhes da tarefa!")


def remover_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]
        tarefas.pop(indice)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")


def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        for t in tarefas:
            linha = f"{t['tarefa']} | Categoria: {t['categoria']} | Prioridade: {t['prioridade']}\n"
            arquivo.write(linha)
    messagebox.showinfo("Sucesso", "Tarefas salvas com sucesso!")


def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    for t in tarefas:
        lista_tarefas.insert(tk.END, f"{t['tarefa']} (Categoria: {t['categoria']}, Prioridade: {t['prioridade']})")


janela = tk.Tk()
janela.title("Gerenciador de Tarefas")


entrada_tarefa = tk.Entry(janela, width=40)
entrada_tarefa.pack(pady=5)
entrada_tarefa.insert(0, "Descrição da tarefa")


entrada_categoria = tk.Entry(janela, width=40)
entrada_categoria.pack(pady=5)
entrada_categoria.insert(0, "Categoria da tarefa")


entrada_prioridade = tk.Entry(janela, width=40)
entrada_prioridade.pack(pady=5)
entrada_prioridade.insert(0, "Prioridade (Alta, Média, Baixa)")


btn_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(pady=5)


lista_tarefas = tk.Listbox(janela, width=60, height=10)
lista_tarefas.pack(pady=10)


btn_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
btn_remover.pack(pady=5)


btn_salvar = tk.Button(janela, text="Salvar Tarefas", command=salvar_tarefas)
btn_salvar.pack(pady=5)


janela.mainloop()