"""Ordenar uma lista: Escreva uma função que ordene uma lista de números em ordem crescente ou decrescente.
"""


def Ordenando_list(lista, ordem):
    if ordem == 1:
        return sorted(lista)
    else:
        return sorted(lista, reverse=True)


def main():
    lista = []
    for n in range(5):
        num = int(input('Numero: '))
        lista.append(num)
    ordem = int(input('[1] Ordem crescente ou [2] decescente:'))
    lista_ordenada = Ordenando_list(lista, ordem)
    if lista_ordenada is not None:
        print(lista_ordenada)
    else:
        print('Lista vazia!')


if __name__ == '__main__':
    main()