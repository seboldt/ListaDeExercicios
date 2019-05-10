n = int(input('informe um numero inteiro \n'))

anterior = 0
agora = 1


for x in range(1, n):

    fibonacci = agora + anterior
    anterior = agora
    agora = fibonacci


    print(fibonacci)
