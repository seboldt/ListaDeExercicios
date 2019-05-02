import math

a = float(input('informe o valor de a\n'))
b = float(input('informe o valor de b\n'))
c = float(input('informe o valor de c\n'))

if a == 0:
    print('não é equação de segundo grau')
else:
    d = (math.pow(b, 2)) - (4 * a *c)

    if d < 0:
        print('a equação não possui raiz')

    elif d == 0:
        print('a equacao possui uma raiz')
        raiz = -(b) / (2 * a)
        print(f'Raiz: {raiz}')

    else:
        print('a equiação possui duas raiz')

        raiz1 = ((-(b) + math.sqrt(d)) / (2 * a))
        raiz2 = ((-(b) - math.sqrt(d)) / (2 * a))

        print(f'raiz1: {raiz1}')
        print(f'raiz2: {raiz2}')

