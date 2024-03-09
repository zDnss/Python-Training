"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""


def main():
    vetor = []
    for n in range(10):
        vetor.append(int(input(f'Digite o {n+1}º valor: ')))
    for i in range(len(vetor) - 1, -1, -1):
        print(vetor[i])


if __name__ == '__main__':
    main()