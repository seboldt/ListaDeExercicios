l = float(input('Informe a quantidade de combustivel abastecido \n'))
tipo = input('Tipo de combustivel \nA-Álcool \nG-Gasolina \n')

valorA = 1.9
valorG = 2.5


if tipo == 'a' or tipo == 'A':

    if l <= 20:
        ValorTotal = (valorA * l) - ((valorA * l) * 0.03 )
    else:
        ValorTotal = (valorA * l) - ((valorA * l) * 0.05)

elif tipo == 'g' or tipo == 'G':
    if l <= 20:
        ValorTotal = (valorG * l) - ((valorG * l) * 0.04)
    else:
        ValorTotal = (valorG * l) - ((valorG * l) * 0.06)
else:
    print('tipo de combustivel invalido \n')



print(f'Total a pagar: {ValorTotal}')