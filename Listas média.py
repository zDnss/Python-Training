def main():
    notas = []
    for n in range(1, 5):
        notas.append(float(input(f'Digite a {n}º nota: ')))
    média = sum(notas) / len(notas)
    print(f'Notas digitadas: {notas}')
    print(f'Média final do aluno: {média}')


if __name__ == '__main__':
    main()