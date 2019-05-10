n1 = int(input('infomre um numero \n'))
n2 = int(input('informe outro numero \n'))

total = n1

for x in range(0, n2-1):
    total = total * n1

print(f'resultado de {n1} elevado a {n2} é {total}')