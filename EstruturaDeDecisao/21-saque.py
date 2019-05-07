saque = int(input('informe o valor do saque (valor inteiro) \n'))


if saque < 10 or saque > 600:
    print('valor invalido para saque')
else:

    nota100 = saque / 100

    nota50 = (saque - (int(nota100) * 100)) / 50

    if int(nota50) != 0:
        nota10 = ((saque - (int(nota100) * 100)) - 50) / 10

    else:
        nota10 = (saque - (int(nota100) * 100)) / 10


    nota5 = (saque - ((int(nota100) * 100) + (int(nota50) * 50) + (int(nota10) * 10))) / 5

    nota1 = saque - ((int(nota100) * 100) + (int(nota50) * 50) + (int(nota10) * 10) + (int(nota5) * 5))

    print(int(nota100))
    print(int(nota50))
    print(int(nota10))
    print(int(nota5))
    print(int(nota1))