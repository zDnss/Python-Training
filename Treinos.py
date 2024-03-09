"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:"""
lista = ("Telefonou para a vítima?",
         "Esteve no local do crime?",
         "Mora perto da vítima?",
         "Devia para a vítima?",
         "Já trabalhou com a vítima?")


def main():
    contador = 0
    for n in lista:
        perguntas = input(f'{n}: ').lower()
        if perguntas in ['s', 'sim']:
            contador += 1
    if contador < 2:
        print('Inocente')
    elif contador == 2:
        print('Suspeito')
    elif contador in range(3, 5):
        print('Cumplice')
    elif contador == 5:
        print('Assassino')


if __name__ == '__main__':
    main()
