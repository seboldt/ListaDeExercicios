respostas = []

print('Responda S ou N para as perguntas')
respostas.append(input('Telefonou para a vitima \n').upper())
respostas.append(input('Esteve no local do crime \n').upper())
respostas.append(input('Mora perto da vitima \n').upper())
respostas.append(input('Devia para a vitima \n').upper())
respostas.append(input('Ja trabalhou com a vitima \n').upper())

n = respostas.count('S')

resultado = ''

if n == 2:
    resultado = 'Suspeita'
elif n == 3 or n == 4:
    resultado = 'Cumplice'
elif n == 5:
    resultado = 'Assassino'
else:
    resultado = 'Inocente'

print(f'Resultado: {resultado}')