n1 = int(input('informe um numero inteiro \n'))
n2 = int(input('informe outro numero inteiro \n'))


if n1 > n2:
    for x in range(n2, n1):
        print(x)

elif n2 > n1:
    for x in range(n1, n2):
        print(x)

else:
    print('numeros iguais')