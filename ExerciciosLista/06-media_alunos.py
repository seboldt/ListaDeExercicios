media = []

for x in range(0, 10):
    print(f'Aluno: {x} \n')
    nota = []
    for i in range(0, 4):
        nota.append(int(input(f'nota {i} bimestre \n')))

    media.append(nota)

aluno = 0

for nota in media:
    m = (nota[0] + nota[1] + nota[2] + nota[3]) / 4
    print(f'Média: {m}')
    if m >= 7:
        aluno += 1

print(f'Alunos na média: {aluno}')


