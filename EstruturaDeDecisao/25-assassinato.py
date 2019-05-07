print('Depoimento \nResponda apenas s ou n')
r1 = input('Telefonou p/ a vitima ? \n')

classificacao = 0

if r1 == 's':
    classificacao += 1

r2 = input('Esteve no local do crime ?\n')

if r2 == 's':
    classificacao += 1
r3 = input('Mora perto da Vitima ? \n')

if r3 == 's':
    classificacao += 1
r4 = input('Devia para a vitima ? \n')

if r4 == 's':
    classificacao += 1

r5 = input('Já trabalhou com a vitima ? \n')

if r5 == 's':
    classificacao += 1


if classificacao == 2:
    print('Suspeito')
elif classificacao >=3 and classificacao <=4:
    print('Cumplice')
elif classificacao == 5:
    print('Assassino')
else:
    print('Inocente')
