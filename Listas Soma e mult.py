"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""


def soma_mult(vetor):
    soma = sum(vetor)
    multiplication = 1
    for n in vetor:
        multiplication *= n
    return soma, multiplication


def main():
    vetor = []
    for n in range(5):
        vetor.append(int(input('Digite um num: ')))
    soma, multiplication = soma_mult(vetor)
    print(f'Numeros digitados {vetor}')
    print(f'Soma de todos os numeros {soma}')
    print(f'Multiplicação de todos os numeros {multiplication}')


if __name__ == '__main__':
    main()
