pessoas = []

for x in range(0, 5):
    pessoa = []
    pessoa.append(input('informe sua altura \n'))
    pessoa.append(input('informe sua idade \n'))
    pessoas.append(pessoa)

pessoas.reverse()

print(pessoas)

for pessoa in pessoas:
    print(f'Idade {pessoa[0]} - Altura: {pessoa[1]}')