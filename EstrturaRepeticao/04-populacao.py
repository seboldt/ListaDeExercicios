import math

a = 80000
b = 200000
ano = 0

while b > a:
    ano +=1
    a = a + (a * 0.03)
    b = b + (b * 0.015)
    print(f'Ano {ano}')
    print(f'Populacao A: {math.ceil(a)}')
    print(f'Populacao B: {math.ceil(b)}')