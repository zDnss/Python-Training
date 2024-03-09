import tkinter as tk

xy = "300x300"
azul_claro = "#5F9F9F"
cinza = "#2E353D"
cinza_claro1 = "#F0FfF9"
cinza_claro2 = "#666666"
tamanho_fonte = 12
fonte = ('Helvetica', tamanho_fonte, 'bold')
fonte_creditos = ('Courier', 9, 'bold')

root = tk.Tk()
root.title('Beeping Automator')
root.geometry(xy)
root.resizable(False, False)

def bot1():
    """
    Este é um exemplo de aplicativo tkinter com funcionalidade de automação usando PyAutoGUI.
    Ele permite que o usuário insira informações sobre caixas e medidores e, em seguida, inicie a automação
    para inserir os dados conforme necessário.

    Instruções de uso:
    - Preencha os campos com as informações necessárias.
    - Clique no botão 'SAVE' para guardar as informações.
    - Clique no botão 'START' para iniciar a automação.

    @author: Dns
    """
    import random
    import pyautogui as pg
    import tkinter as tk
    from time import sleep

    # Lista onde guarda os codigos de fechamento
    codigos = []

    xy = "300x400"
    azul_claro = "#5F9F9F"
    cinza = "#2E353D"
    cinza_claro1 = "#F0FfF9"
    cinza_claro2 = "#666666"
    tamanho_fonte = 9
    fonte = ('Helvetica', tamanho_fonte, 'bold')
    fonte_creditos = ('Courier', 9, 'bold')

    root = tk.Tk()
    root.title("Beeping Automator")
    root.geometry(xy)
    root.resizable(False, False)
    root.iconbitmap("C:\\Users\\denilson.bessa.ELETRA\\PycharmProjects\\pythonProject\\automatic_logo_icon_145470.ico")

    def iniciar_programa():
        """
        Função que inicia o programa de automação.
        """
        # Obter informações inseridas pelo usuário
        texto_caixas, texto_primeira_caixa, texto_medidores_caixa, texto_primeiro_codigo, contagem, texto_prefix_codigo, prefix_codigo_loop = guardar_texto()
        medidores_inteiro = int(texto_medidores_caixa)

        # Abrir o navegador Chrome
        pg.click(406, 741)  # Chrome
        sleep(1)

        # Mover o cursor para a entrada de dados
        pg.moveTo(261, 222)  # Move para a entrada de dados
        pg.click()
        pg.hotkey('ctrl', 'a')

        # Escrever o código do primeiro medidor
        sleep(1)
        if prefix_codigo_loop == False:
            pg.typewrite(str(texto_primeiro_codigo), interval=0)
            pg.press('enter')
        else:
            pg.typewrite(texto_prefix_codigo + str(texto_primeiro_codigo), interval=0)
            pg.press('enter')

        # Loop para inserir códigos de medidores para cada caixa
        print('<LOG')
        for c in range(int(texto_caixas) - 1):
            # Imprime a contagem para cada caixa
            print(f'    {contagem}')
            codigos.append(contagem)
            sleep(0.5)
            if prefix_codigo_loop:
                pg.typewrite(texto_prefix_codigo + str(contagem), interval=0)
            else:
                pg.typewrite(str(contagem), interval=0)
            pg.press('enter')

            # Adiciona a quantidade de medidores na caixa atual
            contagem += medidores_inteiro
        print('          LOG>')
        sleep(1)
        # Escrever um código especial no final
        pg.typewrite(str('00000000'), interval=0)
        pg.press('enter')

    def guardar_texto():
        """
        Função para obter os valores inseridos pelo usuário.
        """

        texto_caixas = caixas_entry.get()  # Obtém o texto inserido no campo "QUANTIDADE DE CAIXAS"
        texto_medidores_caixa = medidores_caixas_entry.get()  # Obtém o texto inserido no campo "QUANTIDADE DE MEDIDORES POR CAIXA"
        texto_primeira_caixa = primeira_caixa_entry.get()  # Obtém o texto inserido no campo "QUANTIDADE DE MEDIDORES NA PRIMEIRA CAIXA"
        texto_primeiro_codigo = primeiro_codigo_entry.get()  # Obtém o texto inserido no campo "CODIGO DO PRIMEIRO MEDIDOR"
        prefix_codigo_loop = True  # Define a variável prefix_codigo_loop como True por padrão
        texto_prefix_codigo = prefix_codigo_entry.get()  # Obtém o texto inserido no campo "PREFIXO (0 SE NÃO HOUVER)"

        if texto_prefix_codigo == '0':  # Verifica se o texto do campo "PREFIXO (0 SE NÃO HOUVER)" é '0'
            prefix_codigo_loop = False  # Se for, define prefix_codigo_loop como False

        contagem = int(texto_primeiro_codigo) + int(
            texto_primeira_caixa)  # Calcula a contagem somando o valor inserido no campo "CODIGO DO PRIMEIRO MEDIDOR" com o valor inserido no campo "QUANTIDADE DE MEDIDORES NA PRIMEIRA CAIXA"

        return texto_caixas, texto_primeira_caixa, texto_medidores_caixa, texto_primeiro_codigo, contagem, texto_prefix_codigo, prefix_codigo_loop  # Retorna todos os textos e variáveis calculadas

    def fechar_palete():
        texto_caixas, texto_primeira_caixa, texto_medidores_caixa, texto_primeiro_codigo, contagem, texto_prefix_codigo, prefix_codigo_loop = guardar_texto()

        sleep(3)
        if not prefix_codigo_loop:
            for n in range(2):
                pg.typewrite(str(codigos[n]), interval=1)
                pg.press('enter')
                pg.press('tab')
        else:
            for n in range(2):
                pg.typewrite(texto_prefix_codigo + str(codigos[n]), interval=1)
                pg.press('enter')
                pg.press('tab')

    # Carregar a imagem de plano de fundo
    imagem_fundo = tk.PhotoImage(
        file='C:\\Users\\denilson.bessa.ELETRA\\PycharmProjects\\pythonProject\\wp_bdi_096.png')
    fundo_label = tk.Label(root, image=imagem_fundo)
    fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Outros widgets
    caixas = tk.Label(root, text='QUANTIDADE DE CAIXAS', font=fonte, background=cinza,
                      fg='white')  # Pede a quantidade de caixas
    caixas.pack(padx=10)
    caixas_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
    caixas_entry.pack(pady=5)

    medidores_caixas = tk.Label(root, text='QUANTIDADE DE MEDIDORES POR CAIXA', font=fonte, background=cinza,
                                fg='white')  # Pede a quantidade de medidores
    medidores_caixas.pack(pady=5)
    medidores_caixas_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
    medidores_caixas_entry.pack(pady=5)

    primeira_caixa = tk.Label(root, text='QUANTIDADE DE MEDIDORES NA PRIMEIRA CAIXA', font=fonte, background=cinza,
                              # Pede a quantidade de medidores na primeira caixa
                              fg='white')
    primeira_caixa.pack(pady=5)
    primeira_caixa_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
    primeira_caixa_entry.pack(pady=5)

    primeiro_codigo = tk.Label(root, text='CODIGO DO PRIMEIRO MEDIDOR', font=fonte, background=cinza,
                               fg='white')  # Pede o codigo do primeiro medidor
    primeiro_codigo.pack(pady=5)
    primeiro_codigo_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
    primeiro_codigo_entry.pack(pady=5)

    prefix_codigo = tk.Label(root, text='PREFIXO (0 SE NÃO HOUVER)', font=fonte, background=cinza,
                             fg='white')  # Pede o prefixo, se não houver digita 0(Todo resto considera prefixo)
    prefix_codigo.pack(pady=5)
    prefix_codigo_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
    prefix_codigo_entry.pack(pady=5)

    botao_iniciar = tk.Button(root, text='START', font=('Press Start 2P', 12, 'bold'),
                              command=iniciar_programa)  # Botao start Chama a função iniciar programa e a magica acontece
    botao_iniciar.config(bg=cinza_claro2)
    botao_iniciar.pack(pady=10)

    botao_fechar = tk.Button(root, text='FECHAR PALETE', font=('Press Start 2P', 9, 'bold'), command=fechar_palete)
    botao_fechar.config(bg=cinza_claro2)
    botao_fechar.place(x=100, y=347)

    dev = tk.Label(root, font=fonte_creditos, text='@Author: Denilson', background=cinza, fg='white')  # Author Credits
    dev.place(x=85, y=380)

    root.mainloop()


beeper = tk.Label(root, text='Beeper Automator', font=fonte, bg=cinza_claro1)
beeper.pack()
botao_beeper = tk.Button(root, text='V1', command=bot1)
botao_beeper.config(width=10, bg=cinza_claro2, fg='white', font=fonte)
botao_beeper.pack(pady=2)

nfs = tk.Label(root, text="NF's Automator", font=fonte, bg=cinza_claro1)
nfs.pack(pady=5)
botao_nfs = tk.Button(root, text='V1')
botao_nfs.config(width=10, bg=cinza_claro2, fg='white', font=fonte)
botao_nfs.pack(pady=2)


root.mainloop()
