data = (input('Informe a data no formato dd/mm/aaaa \n'))

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

bissexto = False

if ano % 4 == 0:
    bissexto = True
    if ano % 100 == 0 and ano % 400 != 0:
        bissexto = False

dataValida = True

if mes in (1, 3, 5, 7, 8, 10, 12):
    if dia < 1 or dia > 31:
        dataValida = False

elif mes in (4, 6, 9, 11):
    if dia < 1 or dia > 31:
        dataValida = False

elif bissexto == True and mes == 2:
    if dia < 1 or dia > 29:
        dataValida = False

elif bissexto == False and mes == 2:
    if dia <1 or dia > 28:
        dataValida = False


if dataValida:
    print(f'Data valida: {dia}/{mes}/{ano}')

else:
    print('Data invalida')
