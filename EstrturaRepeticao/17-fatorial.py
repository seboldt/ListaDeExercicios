n = int(input('informe um numero inteiro \n'))

resultado = n

for x in range(1, n):
    resultado = resultado * (n - 1)
    print(f' {n}. ', end="")
    n-=1


print(f'= {resultado}')