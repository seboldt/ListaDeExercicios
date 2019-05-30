n = []
for x in range(0,10):
    n.append(float(input('informe um numero \n')))

quadrado = []

soma = 0
for i in range(0,10):
    quadrado.append(n[i] * n[i])
    soma = soma + quadrado[i]

print(n)
print(quadrado)
print(soma)


