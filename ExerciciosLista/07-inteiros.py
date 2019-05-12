n = []

for x in range(0, 5):
    n.append(int(input('informe um numero inteiro \n')))

soma = 0
multiplicacao = 1

for i in n:
    soma += i
    multiplicacao *= i


print(soma)
print(multiplicacao)
print(n)