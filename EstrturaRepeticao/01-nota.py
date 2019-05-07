nota = -1

while nota < 0 or nota >10:
    nota = float(input('informe uma nota:'))
    if nota < 0 or nota > 10:
        print('Nota invalida')

print(nota)