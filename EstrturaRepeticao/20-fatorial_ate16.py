qtdade = 0
while qtdade <= 0:
    qtdade = int(input('Informe a quantidade de fatoriais a serem calculadas \n'))
    if qtdade <= 0:
        print('quantidade deve ser positiva')


for x in range(0, qtdade):
    n = 17
    while n > 16:
        n = int(input('informe um numero inteiro \n'))
        if n > 16:
            print('o numero deve ser maior que 16')

    resultado = n

    print(f'{n}! =', end="")

    for x in range(1, n):
        resultado = resultado * (n - 1)
        print(f' {n} x', end="")
        n-=1
    print(' 1 ', end="")
    print(f'= {resultado}')