def Palindromo(palavra):    # Função em que vai comparar a palavra
    print(f'Palavra {palavra}, De trás pra fente: {palavra[::-1]}')
    if palavra == palavra[::-1]:    # se for igual imprime palindromo
        print('É um palindromo')
    else: # Fala se não for
        print('Não é um palindromo!')


def main():
    palavra = str(input('Digite uma palavra: ')).lower()     # Pede a palavra
    Palindromo(palavra)


if __name__ == '__main__':
    main()