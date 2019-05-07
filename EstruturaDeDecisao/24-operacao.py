n1 = float(input('informe primeiro numero \n'))
n2 = float(input('informe segundo numero \n'))


conta = int(input('Informe tipo de conta \n1- Somar \n2-Subtrair \n3-Multiplicar \n4-Dividir \n'))

if conta == 1:
    resultado = n1 + n2
elif conta == 2:
    resultado = n1 - n2
elif conta == 3:
    resultado = n1 * n2
elif conta == 4:
    resultado = n1 / n2
else:
    print('numero informa nao corresponde')


print(f'Resultado: {resultado}')

if resultado % 2 == 0:
    print('Resultado é par')
else:
    print('Resultado é Impar')

if resultado >= 0:
    print('Positivo')
else:
    print('Negativo')


if resultado == int(resultado):
    print('Inteiro')
else:
    print('Decimal')