"""
Crie um dicionário que represente um catálogo de produtos de uma loja.
Cada chave deve ser o nome de um produto e cada valor deve ser o preço desse produto.
"""

# Definição do catálogo de produtos da loja como um dicionário onde as chaves são os nomes dos produtos e os valores
# são os preços
loja = {
    'Camiseta': 25.99,
    'Calça Jeans': 49.99,
    'Tênis': 79.99,
    'Relógio': 99.99,
    'Mochila': 39.99,
    'Óculos de Sol': 29.99,
    'Boné': 14.99,
    'Jaqueta de Couro': 149.99,
    'Cinto de Couro': 19.99,
    'Bermuda': 34.99,
    'Sapato Social': 89.99,
    'Camisa Social': 59.99,
    'Carteira': 9.99,
    'Pulseira': 4.99,
    'Brincos': 8.99,
    'Moletom': 54.99,
    'Chapéu': 24.99,
    'Lenço': 12.99,
    'Meias': 6.99,
    'Luvas': 11.99,
    'Agenda': 7.99,
    'Caneca': 3.99,
    'Cachecol': 19.99,
    'Blusa de Frio': 39.99,
    'Saia': 29.99,
    'Vestido': 69.99,
    'Bolsa de Couro': 79.99,
    'Gravata': 16.99,
    'Porta-cartões': 5.99,
    'Brinquedo de Pelúcia': 19.99
}


# Solicitação do limite de compra ao usuário
limite = float(input('Digite o limite da compra: '))

# Exibe os itens cujo preço é superior ao limite fornecido
print('Seu limite é menor que esses itens:')
for produto, preco in loja.items():
    if limite < preco:
        print(f'Item {produto} tem o valor de R${preco:.2f}')
print()
# Exibe os itens cujo preço é igual ou inferior ao limite fornecido
print('Seu limite é válido para esses itens:')
for produto, preco in loja.items():
    if limite >= preco:
        print(f'Item {produto} tem o valor de R${preco:.2f}')
