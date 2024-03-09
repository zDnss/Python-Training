import tkinter as tk
from tkinter import messagebox

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()

    if nome.strip() == '' or email.strip() == '':
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    else:
        messagebox.showinfo("Cadastro", f"Usuário cadastrado:\nNome: {nome}\nEmail: {email}")

# Criando a janela
root = tk.Tk()
root.title("Cadastro de Usuário")

# Criando os widgets
label_nome = tk.Label(root, text="Nome:")
label_email = tk.Label(root, text="Email:")
entry_nome = tk.Entry(root)
entry_email = tk.Entry(root)
button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
button_cancelar = tk.Button(root, text="Cancelar", command=root.destroy)

# Posicionando os widgets na janela
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nome.grid(row=0, column=1, padx=5, pady=5)
label_email.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_email.grid(row=1, column=1, padx=5, pady=5)
button_cadastrar.grid(row=2, column=0, padx=5, pady=5)
button_cancelar.grid(row=2, column=1, padx=5, pady=5)

# Rodando o loop principal da aplicação
root.mainloop()
