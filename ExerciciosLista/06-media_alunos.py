media = []
nota = []

for x in range(1, 11):
    print(f'Notas aluno {x} \n')
    n1 = float(input('Informe a nota do Primeiro bimestre \n'))
    n2 = float(input('Informe a nota do Segundo bimestre \n'))
    n3 = float(input('Informe a nota do Terceiro bimestre \n'))
    n4 = float(input('Informe a nota do Quarto bimestre \n'))
    media.append((n1 + n2 + n3 + n4) / 4)

alunos = 0

for i in range(0, 10):
    if media[i] >= 7:
        alunos += 1


print(f'{alunos} Alunos aprovados ')



