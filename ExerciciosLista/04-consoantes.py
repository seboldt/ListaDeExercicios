vogais = ['A', 'E', 'I', 'O', 'U']
letra = []
consoantes = []

for x in range(0, 10):
    letra.append(input('informe um caracter \n').upper())

total = 0

for x in range(0, 10):
    if letra[x] not in vogais:
        consoantes.append(letra[x])
        total += 1


print(consoantes)
print(total)
