n = int(input('Informe a quantidade de repetições \n'))

num = int(input('informe um numero inteiro \n'))
maior = num
menor = num

for x in range(n-1):
    num = int(input('informe um numero inteiro \n'))
    if num > maior:
        maior = num

    elif num < menor:
        menor = num

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')