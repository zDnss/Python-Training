# Solicita ao usuario uma sequencia de numeros separados por ,
entrada = input('Digite uma sequencia de numeros separados por ",": ')

# Divide a entrada usando a virgula como delimitador e converte os numeros para inteiros
numeros = list(map(int, entrada.split(',')))

# Soma da lista de numeros dividido pela quantidade de itens na lista
media = sum(numeros) / len(numeros)

# Imprime a lista completa, a soma e a media dos numeros digitados
print(f'Os numeros digitados foram {numeros}')
print(f'A soma dos numeros é {sum(numeros)}')
print(f'A media dos numeos é {media}')