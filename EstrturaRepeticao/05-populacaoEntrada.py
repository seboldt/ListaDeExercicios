import math
import sys

a = int(input('Informe a populacao do primeiro país \n'))
b = int(input('Informe a populacao do segundo país \n'))
taxaA = -1
taxaB = -1

while taxaA < 0 or taxaA > 100:
    taxaA = float(input('Informe a taxa de crescimento do primeiro país \n')) / 100
    if taxaA < 0 or taxaA > 100:
        print('Taxa deve ser entre 0 e 100')

while taxaB < 0 or taxaB > 100:
    taxaB = float(input('Informe a taxa de crescimento do segundo país \n')) / 100
    if taxaB < 0 or taxaB > 100:
        print('Taxa deve ser entre 0 e 100')
ano = 0

if b > a and taxaB > taxaA:
    print('Primeiro país não pode ser maior que segundo país')
    sys.exit()
elif a > b and taxaA > taxaB:
    print('O segundo país não pode ser maior que o primeiro')
    sys.exit()

if b > a:
    while b > a:
        ano +=1
        a = a + (a * taxaA)
        b = b + (b * taxaB)
        print(f'Ano {ano}')
        print(f'Populacao A: {math.ceil(a)}')
        print(f'Populacao B: {math.ceil(b)}')

elif a > b:
    while a > b:
        ano +=1
        a = a + (a * taxaA)
        b = b + (b * taxaB)
        print(f'Ano {ano}')
        print(f'Populacao A: {math.ceil(a)}')
        print(f'Populacao B: {math.ceil(b)}')

