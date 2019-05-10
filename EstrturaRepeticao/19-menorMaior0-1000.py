n = int(input('Informe a quantidade de repetições \n'))

maior = 1001
menor = -1
num = -1
for x in range(n):

    if num < 0 or num > 1000:
        print('deve informar um numero entre 0 e 1000 \n')
        while num < 0 or num > 1000:
            num = int(input('infomre um numero entre 0 e 1000 \n'))
    else:
        num = int(input('informe um numero entre 0 e 1000 \n'))

    if num > maior:
        maior = num

    elif num < menor:
        menor = num

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')