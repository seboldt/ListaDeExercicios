morango = float(input('informe a quantidade de morango comprado \n'))
maca = float(input('informe a quantidade de maça comprada \n'))

if morango <= 5:
    pMorango = 2.5
else:
    pMorango = 2.2

if maca <= 5:
    pMaca = 1.8
else:
    pMaca = 1.5

total = maca * pMaca + morango * pMorango

if maca + morango >= 8 or total >= 25:
    total = total - (total * 0.1)

print(total)