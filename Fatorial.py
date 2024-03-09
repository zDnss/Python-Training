def calcular_fatorial(num):
    fatorial = 1
    for n in range(1, num+1):
        fatorial *= n
    return fatorial

def main():
    num = int(input('Digite um numero inteiro: '))
    resultado = calcular_fatorial(num)
    print(f'O fatorial de {num} é {resultado}')

if __name__ == '__main__':
    main()