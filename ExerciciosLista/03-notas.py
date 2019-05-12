notas = []
soma = 0
for x in range(0,4):
    notas.append(float(input('informe a nota do aluno de 0 a 10 \n')))
    soma = soma + notas[x]

for x in range(0 ,4):
    print(f' {notas[x]} ',  end="")
print(f' = Mẽdia do aluno: {soma / 4}')



