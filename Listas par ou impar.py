"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""


def par_ou_impar(vetor):
    par = []
    impar = []
    for i in vetor:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    return par, impar


def main():
    vetor = []
    for n in range(2):
        vetor.append(int(input(f'Digite o {n+1}º numero: ')))
    par, impar = par_ou_impar(vetor)
    print(f'Numeros digitados: {vetor}')
    print(f'Todos os numeros pares {par}')
    print(f'Todos os numeos impares {impar}')


if __name__ == '__main__':
    main()
