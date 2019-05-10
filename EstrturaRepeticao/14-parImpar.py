par = 0
impar = 0
for x in range(10):
    n = int(input('informe um numero inteiro \n'))

    if n % 2 == 0:
        par +=1
    else:
        impar +=1

print(f'{par} números par e {impar} números impares')