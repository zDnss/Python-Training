"""Soma dos elementos: Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.
"""


def Soma(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma


def main():
    lista = []
    for n in range(5):
        num = int(input('Digite um numero: '))
        lista.append(num)
    soma_dos_numeros = Soma(lista)
    print(soma_dos_numeros)


if __name__ == '__main__':
    main()
