cont1, cont2, cont3, cont4 = 0, 0, 0, 0


def numeros(num):
    global cont1, cont2, cont3, cont4
    # Função para calcular quantos numeros existem em cada intervalo

    if 0 <= num <= 25:
        cont1 += 1
    elif 26 < num <= 50:
        cont2 += 1
    elif 50 < num <= 75:
        cont3 += 1
    elif 75 < num <= 100:
        cont4 += 1


def main():
    # Pede um numero positivo, um negativo para, ValueError tratado,
    while True:
        try:
            num = int(input('Digite um numero positivo! -1 para: '))
            if num > 100:
                print('Digite um numero maior que 0!')
        except ValueError:
            print('Digite um numero!')
        numeros(num)
        if num < 0:
            break
    print(f'Entre 0 e 25 existem {cont1}')
    print(f'Entre 26 e 50 existem {cont2}')
    print(f'Entre 51 e 75 existem {cont3}')
    print(f'Entre 76 e 100 existem {cont4}')


if __name__ == '__main__':
    main()
