import pyautogui as pg
from time import sleep


def fechar_caixas():
    sleep(1)
    pg.click(406, 741) # Chrome
    sleep(5)
    pg.moveTo(23,601) # Pallets
    pg.click()
    sleep(1)
    pg.click(27, 631) # Paletes abertos
    sleep(1)
    pg.click(30, 691) # Fechar
    sleep(1)
    pg.moveTo(261, 222) # Move para a entrada de dados


def calcular_medidores_por_caixa():
    """
    Função para calcular a numeração final dos medidores em um palete de caixas.

    # Solicita ao usuário a quantidade de caixas, a quantidade de medidores por caixa,
    # a quantidade de medidores na primeira caixa e o código do primeiro medidor da caixa.
    # Em seguida, calcula a numeração final dos medidores somando a numeração inicial
    # (código do primeiro medidor + quantidade de medidores na primeira caixa)
    # com a quantidade de medidores nas caixas restantes.

    Exceções:
        - ValueError: É levantada se o usuário digitar algo que não seja um número inteiro.

    Exemplo de uso:
        calcular_medidores_por_caixa()
    """
    try:
        # Solicita a quantidade de caixas ao usuário
        qtd_caixas = int(input('Quantidade de caixas: '))
        # Solicita a quantidade de medidores por caixa ao usuário
        qtd_medidores = int(input('Quantidade de medidores por caixa: '))
        # Solicita a quantidade de medidores na primeira caixa ao usuário
        caixa_1 = int(input('Quantos medidores tem na caixa 1: '))
        # Solicita o código do primeiro medidor da caixa ao usuário
        codigo_medidor = int(input('Digite o codigo do 1º medidor da caixa: '))
        # Calcula a numeração inicial dos medidores
        contagem = codigo_medidor + caixa_1
        fechar_caixas()
        sleep(2)
        pg.typewrite(str(codigo_medidor), interval=0)
        pg.press('enter')

        # Loop para calcular a numeração final dos medidores nas caixas restantes
        for c in range(qtd_caixas-1):
            # Imprime a contagem para cada caixa
            print(contagem)
            sleep(1)
            pg.typewrite(str(contagem), interval=0)
            pg.press('enter')

            contagem += qtd_medidores  # Adiciona a quantidade de medidores na caixa atual
        sleep(1)
        pg.typewrite(str('00000000'), interval=0)
        pg.press('enter')
    except ValueError:
        # Exibe uma mensagem de erro se o usuário inserir algo que não seja um número inteiro
        print('Digite apenas numeros inteiros')


calcular_medidores_por_caixa()
