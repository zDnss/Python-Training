"""
Crie um programa que permita ao usuário adicionar disciplinas e notas ao dicionário de notas do aluno
até que ele decida parar de inserir. Em seguida, exiba o dicionário completo.
"""

alunos = {}

cont = 0

while True:
    notas = []
    materia = str(input('Matéria: '))

    # Loop para inserção de notas
    while True:
        cont += 1
        n = float(input(f'Nota nº{cont} (999 Encerra!): '))
        if n == 999:
            break
        notas.append(n)

    # Reinicia contador para próxima matéria
    cont = 0

    # Armazena as notas no dicionário de notas do aluno
    alunos[materia] = notas[:]

    # Limpa a lista de notas para a próxima matéria
    notas.clear()

    # Verifica se o usuário deseja continuar adicionando matérias e notas
    resp = str(input('Quer continuar? S/N: '))
    if resp.lower() != 's':
        break

# Exibe o dicionário completo de notas do aluno
for materia, notas in alunos.items():
    print(f'Matéria: {materia}, Notas: {notas}')
