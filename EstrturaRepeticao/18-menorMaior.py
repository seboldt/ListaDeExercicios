rep = -1
soma = 0



while rep < 0:
    rep = int(input('informe o numero de repeticoes \n'))
    if rep < 0:
        print('o numero de repeticoes deve ser maior que 0 \n')

    for x in range(0, rep):
        n = int(input('informe um numero \n'))
        soma = soma + n
        if 'maior' not in vars() or n > maior:
            maior = n
        elif 'menor' not in vars() or n < menor:
            menor = n

print(maior)
print(menor)
print(soma)