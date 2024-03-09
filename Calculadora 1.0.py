#lembrar se for em float o p4
import tkinter as tk
import math

# Define uma fonte para uso nos widgets
fonte_1 = ('Press Start 2P', 11, 'bold')

# Cria a janela principal
root = tk.Tk()
root.title('CALCULADORA DE PALETES')  # Define o título da janela
root.geometry("600x500")  # Define as dimensões da janela
root.config(bg='gray')  # Define a cor de fundo da janela

# Lista para armazenar temporariamente os paletes
paletes_temp = []

# Lista para armazenar os paletes calculados
paletes = []

# Contador
cont = 0
soma = 0

# Lista para armazenar os medidores por palete
medidores_por_palete = []

# Função para obter as informações inseridas pelo usuário
def guardar_informaçoes():
    texto_peças = peças_entrada.get()
    texto_medidores_caixa = medidores_caixa_entrada.get()
    texto_quantidade_caixas = quantidade_caixas_entrada.get()
    return texto_peças, texto_quantidade_caixas, texto_medidores_caixa

# Função para limpar as entradas de dados e as labels de paletes
def limpar():
    global p1, p2, p3, p4
    paletes.clear()
    peças_entrada.delete(0, tk.END)
    medidores_caixa_entrada.delete(0, tk.END)
    quantidade_caixas_entrada.delete(0, tk.END)
    # Remova as labels dos paletes movendo-as para uma posição fora da janela
    p1.place(x=5000, y=5000)
    p2.place(x=5000, y=5000)
    p3.place(x=5000, y=5000)
    p4.place(x=5000, y=5000)

# Função para calcular os paletes
def calculo():
    global p1, p2, p3, p4, soma
    paletes.clear()
    paletes_temp.clear()
    # Logica para saber a quantidade de caixas por palete
    texto_peças, texto_quantidade_caixas, texto_medidores_caixa = guardar_informaçoes()
    peç = int(texto_peças)
    medid = int(texto_medidores_caixa)

    total_de_caixas = peç / medid
    temp_paletes = []

    while total_de_caixas > int(texto_quantidade_caixas):
        if total_de_caixas >= int(texto_quantidade_caixas):
            temp_paletes.append(int(texto_quantidade_caixas[:]))
            paletes.append(temp_paletes[:])
            temp_paletes.clear()
        total_de_caixas -= int(texto_quantidade_caixas)
    if total_de_caixas.is_integer():
        temp_paletes.append(total_de_caixas)
    else:
        temp_paletes.append(math.ceil(total_de_caixas))
    paletes.append(temp_paletes[:])

    # Mostrar na tela
    if len(paletes) >= 1:
        p1 = tk.Label(root, text=f'Palete 1 = {paletes[0]} Caixas')
        p1.place(x=340, y=10)

    if len(paletes) >= 2:
        p2 = tk.Label(root, text=f'Palete 2 = {paletes[1]} Caixas')
        p2.place(x=340, y=40)
    else:
        p2 = tk.Label(root, text=f'Palete 2 =  [0] Caixas')
        p2.place(x=340, y=40)
    if len(paletes) >= 3:
        p3 = tk.Label(root, text=f'Palete 3 = {paletes[2]} Caixas')
        p3.place(x=340, y=70)
    else:
        p3 = tk.Label(root, text=f'Palete 3 =  [0] Caixas')
        p3.place(x=340, y=70)
    if len(paletes) >= 4:
        p4 = tk.Label(root, text=f'Palete 4 = {paletes[3]} Caixas')
        p4.place(x=340, y=100)
    else:
        p4 = tk.Label(root, text=f'Palete 4 =  [0] Caixas')
        p4.place(x=340, y=100)

    # Logica para saber a quantidade de medidores por palete
    for sublist in paletes:
        for num in sublist:
            numero = int(num) * int(texto_medidores_caixa)
            medidores_por_palete.append(numero)
    #del medidores_por_palete[0]

    palete_01 = int(texto_peças) - sum(medidores_por_palete)
    print(palete_01)



# Labels e entradas para entrada de dados
peças = tk.Label(root, text='Quantidade de peças no lote', font=fonte_1, bg='gray')
peças.grid(pady=12)
peças_entrada = tk.Entry(width=10, justify='center')
peças_entrada.place(x=265, y=13)

medidores_caixa = tk.Label(root, text='Quantidade de medidores por caixa', font=fonte_1, bg='gray')
medidores_caixa.grid(pady=12)
medidores_caixa_entrada = tk.Entry(width=10, justify='center')
medidores_caixa_entrada.place(x=265, y=63)

quantidade_caixas = tk.Label(root, text='Quantidade de caixas por palete', font=fonte_1, bg='gray')
quantidade_caixas.grid(pady=12)
quantidade_caixas_entrada = tk.Entry(width=10, justify='center')
quantidade_caixas_entrada.place(x=265, y=111)

# Botões para calcular e limpar
calcular = tk.Button(root, text='Calcular', width=8, command=calculo)
calcular.place(x=265, y=147)

limpar = tk.Button(root, text='Limpar', width=8, command=limpar)
limpar.place(x=189, y=147)

root.mainloop()
