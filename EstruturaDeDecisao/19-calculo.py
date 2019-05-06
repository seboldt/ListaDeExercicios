n = int(input('informe um numero menor que 1000 \n'))

if n < 1000:
    centenas = n /100
    print('Centenas:',int(centenas))

    dezenas = (n - (int(centenas) * 100)) / 10
    print('Dezenas:', int(dezenas))

    unidades = n - (int(centenas) * 100) - (int(dezenas) * 10)
    print(f'Unidades: {unidades}')
