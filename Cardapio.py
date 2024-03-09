# Cardapio em um dicionario
cardapio = {
    100: {'Especificação': 'Cachorro Quente', 'Preço': 1.20},
    101: {'Especificação': 'Bauru simples', 'Preço': 1.30},
    102: {'Especificação': 'Bauru com ovo', 'Preço': 1.50},
    103: {'Especificação': 'Hambúrguer', 'Preço': 1.20},
    104: {'Especificação': 'Cheeseburguer', 'Preço': 1.30},
    105: {'Especificação': 'Refrigerante', 'Preço': 1.00}
}
total_pedido = 0
# Mostra o cardapio
print('''
Especificação   Código  Preço
Cachorro Frio 100     R$ 1,20
Pedra com areia Simples   101     R$ 1,30
Pão com ovo   102     R$ 1,50
X-Ratão      103     R$ 1,20
Pastel de flango   104     R$ 1,30
Refrigerante de H2O    105     R$ 1,00
''')
print('')
while True:
    try:
        # Verifica se o cliente decidiu encerrar o pedido
        codigo = int(input('Digite o codigo do produto: (0 encerra o pedido): '))

        # Verifica se o cliente decidiu encerrar o pedido
        if codigo == 0:
            break

        # Verifica se o código inserido é válido
        if codigo not in cardapio:
            print('Digite um codigo valido!')
            continue

        # Quantidade de itens do pedido
        while True:
            try:
                quantidade = int(input(f'Quantidade de {cardapio[codigo]['Especificação']}: '))
                if quantidade > 0:
                    break
                else:
                    print('Digite um valor maior que 0!')
            except ValueError:
                print('Digite um valor valido!')

        # Calcula o valor total do item e adiciona ao total do pedido
        valor_item = cardapio[codigo]['Preço'] * quantidade
        total_pedido += valor_item

        # Exibe o item pedido e seu valor total
        print(f'Item {cardapio[codigo]['Especificação']}, Quantidade {quantidade}, Valor R$ {valor_item:.2f}')

    except ValueError:
        print('Digite um valor valido')
print(f'Total do pedido: R$ {total_pedido:.2f}')
