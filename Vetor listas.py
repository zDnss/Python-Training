"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""


def main():
    vetor = []
    for n in range(5):
        num = int(input(f'Digite o {n+1}º numero'))
        vetor.append(num)

    print('Os numeros digitados são:')
    for i in vetor:
        print(i)


if __name__ == '__main__':
    main()