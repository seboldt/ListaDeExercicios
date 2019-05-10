n1 = int(input('informe um numero inteiro \n'))
n2 = int(input('informe outro numero inteiro \n'))

soma = 0

if n1 > n2:
    for x in range(n2, n1):
        print(x)
        soma = soma + x

elif n2 > n1:
    for x in range(n1, n2):
        print(x)
        soma = soma + x

else:
    print('numeros iguais')


print(f'A soma desse range é {soma}')