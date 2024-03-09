impar = 0
par = 0

def ImPar(num):
    global impar, par
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
def main():
    try:
        while True:
            num = int(input('Digite um numero: '))
            ImPar(num)
            continuar = ''
            while continuar not in ['s', 'n']:
                continuar = input('Quer continuar? S/N: ').lower()
            if continuar in 'n':
                break
    except ValueError:
        print('Digite um numero!')
    print(f'Existem {par} numeros pares!')
    print(f'Existem {impar} numeros impares!')

if __name__ == '__main__':
    main()