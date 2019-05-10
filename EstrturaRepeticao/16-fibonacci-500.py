antigo = 0
agora = 1

while agora < 500:
    fibonacci = antigo + agora
    antigo = agora
    agora = fibonacci

    print(fibonacci)
