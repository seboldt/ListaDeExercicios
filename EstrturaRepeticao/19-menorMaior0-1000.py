rep = -1
soma = 0



while rep < 0:
    rep = int(input('informe o numero de repeticoes \n'))
    if rep < 0:
        print('o numero de repeticoes deve ser maior que 0 \n')

    for x in range(0, rep):
        while 'n' not in vars() or n < 0 or n > 1000:
            n = int(input('informe um numero entre 0 e 1000 \n'))
            if n < 0 or n > 1000:
                print('numero deve ser entre 0 e 1000')
        soma = soma + n

        if 'maior' not in vars() or n > maior:
            maior = n
        elif 'menor' not in vars() or n < menor:
            menor = n
        n = -1

print(maior)
print(menor)
print(soma)