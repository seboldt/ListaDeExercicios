ano = float(input('Informe o ano \n'))


if ano % 4 == 0:
    if ano % 100 != 0:
        print('ano bissexto')
    else:
        print('nao é ano bissxto')

elif ano % 4 != 0:
    if ano % 400 == 0:
        print('ano bissexto')
    else:
        print('nao é ano bissexto')