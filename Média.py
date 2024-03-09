def Calculo_media(soma):
    return soma / 3

def main():
    soma = 0
    for n in range(3):
        num = int(input('Digite um numero: '))
        soma += num
    media = Calculo_media(soma)
    print(f'A media dos numeros é {media}')


if __name__ == '__main__':
    main()
