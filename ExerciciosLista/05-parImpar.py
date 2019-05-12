par = []
impar = []

for x in range(0, 20):
    n = int(input('informe um numero inteiro \n'))

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'Par: {par}')
print(f'Impar: {impar}')